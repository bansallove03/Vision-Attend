import os
import cv2


#from EncodeGenerator import studentsIds

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgBackground = cv2.imread('Resources/background.png')

# Importing the mode images into a list


while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    imgBackground[162:162 + 480,55:55 + 640] = img


    #cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)

#find the best match(smallest distance)
            best_match_index = None
            if len(faceDis) > 0:
                best_match_index = faceDis.argmin()

            # Check if the closest face is within the threshold
            if best_match_index is not None and faceDis[best_match_index] < DISTANCE_THRESHOLD:
                matched_student_id = studentsIds[best_match_index]
                matched_distance = faceDis[best_match_index]

                # Print the student ID and the distance that met the threshold
                print(f"Face matched with Student ID: {matched_student_id}")
                print(f"Face matched within the threshold: {matched_distance}")

                # Draw a rectangle around the detected face
                top, right, bottom, left = faceloc
                top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4  # Scale back up (since we resized the image)
                cv2.rectangle(imgBackground, (left + 55, top + 162), (right + 55, bottom + 162), (0, 255, 0), 2)

                # Display the matched student ID on the image
                cv2.putText(imgBackground, f"ID: {matched_student_id}", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0),
                            2)