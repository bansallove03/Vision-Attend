import os
import cv2
import face_recognition
import pickle

# Path to the folder containing student images
folderPath = 'Images'
if not os.path.exists(folderPath):
    raise FileNotFoundError("The 'Images' folder does not exist. Make sure it contains student images.")

# Lists to store the encodings and IDs
imgList = []
studentIds = []

# Read images and IDs from the 'Images' folder
pathList = os.listdir(folderPath)
print("Found images:", pathList)

for path in pathList:
    # Read each image
    imgPath = os.path.join(folderPath, path)
    img = cv2.imread(imgPath)

    if img is not None:
        imgList.append(img)
        # Extract ID from the file name (assumes the file name is the student's ID)
        studentIds.append(os.path.splitext(path)[0])
    else:
        print(f"Could not load image at path: {imgPath}")

print("Student IDs:", studentIds)

# Function to generate face encodings for each image
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        # Convert image to RGB as face_recognition works with RGB images
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Encode the face(s) in the image (assuming one face per image)
        encodes = face_recognition.face_encodings(img)
        if encodes:
            encodeList.append(encodes[0])  # Append only the first encoding
        else:
            print("No face found in an image. Skipping.")
    return encodeList

# Generate encodings and save them to a file
print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

# Save encodings to a pickle file
with open("EncodeFile.p", 'wb') as file:
    pickle.dump(encodeListKnownWithIds, file)
print("Encodings saved to 'EncodeFile.p'")
