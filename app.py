import json
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import threading
import face_attendance  # Import your updated script

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Secret key for session management

# Global variable to track the process
attendance_thread = None

# Load credentials from the JSON file
def load_credentials():
    with open('credentials.json', 'r') as file:
        return json.load(file)

# Save credentials to the JSON file
def save_credentials(username, password):
    with open('credentials.json', 'w') as file:
        json.dump({"username": username, "password": password}, file)

# Get the current credentials
credentials = load_credentials()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == credentials['username'] and password == credentials['password']:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')


@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


@app.route('/reset-credentials', methods=['GET', 'POST'])
def reset_credentials():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        new_username = request.form.get('username')
        new_password = request.form.get('password')

        if new_username and new_password:
            save_credentials(new_username, new_password)
            session.pop('logged_in', None)
            return redirect(url_for('home'))
        else:
            return render_template('reset_credentials.html', error="Both fields are required.")

    return render_template('reset_credentials.html')


@app.route('/start-attendance', methods=['POST'])
def start_attendance():
    global attendance_thread

    if not session.get('logged_in'):
        return jsonify({"message": "Unauthorized access"}), 401

    if attendance_thread is None or not attendance_thread.is_alive():
        face_attendance.stop_attendance = False
        attendance_thread = threading.Thread(target=face_attendance.run_face_attendance)
        attendance_thread.start()
        return jsonify({"message": "Attendance system started successfully."})
    else:
        return jsonify({"message": "Attendance system is already running."})


@app.route('/stop-attendance', methods=['POST'])
def stop_attendance():
    global attendance_thread

    if not session.get('logged_in'):
        return jsonify({"message": "Unauthorized access"}), 401

    if attendance_thread and attendance_thread.is_alive():
        face_attendance.stop_attendance = True
        attendance_thread.join()
        return jsonify({"message": "Attendance system stopped successfully."})
    else:
        return jsonify({"message": "Attendance system is not running."})


if __name__ == '__main__':
    app.run(debug=True)
