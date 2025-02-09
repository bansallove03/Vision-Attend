# Vision-Attend - Facial Recognition Based Attendance System

# Overview
Vision-Attend is an automated attendance system that utilizes facial recognition to mark attendance seamlessly. This project aims to streamline the attendance process by eliminating manual effort and ensuring accuracy.

# Features
- Automated facial recognition for attendance marking
- Secure and efficient student data management
- Real-time attendance tracking
- Excel-based record-keeping with customizable formulae
- User-friendly interface for easy operation

# Tech Stack
- **Programming Language:** Python
- **Libraries Used:** OpenCV, Face Recognition, NumPy, Pandas, Flask, Threading, Openpyxl
- **Database:** Excel-based storage

# Installation & Setup
## Prerequisites
Ensure you have the following installed:
- Latest version of Python
- An IDE to run Python (e.g., PyCharm, VS Code)

## Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/bansallove03/Vision-Attend.git
   cd vision-attend
   ```
2. Create a dedicated folder for the attendance system.
3. Download all required files into the local system.
4. Add students' facial data to the `Images` folder.
5. Install required Python libraries:
   ```sh
   pip install opencv-python face-recognition numpy pandas flask openpyxl threading
   ```
   (This process may take some time.)
6. Run the `EncodeGenerator.py` script (this may take some time).
   - Add student data in an Excel sheet and update formulae as needed.
7. Run the main application:
   ```sh
   python app.py
   ```
8. Start official login and attendance process.
9. Position your face in front of the camera until you see "ATTENDANCE MARKED" in green.

# Contribution
We welcome contributions! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.



# Developer
Love Bansal

