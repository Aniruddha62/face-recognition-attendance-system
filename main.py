import cv2
import face_recognition
import numpy as np
import csv
import os
from datetime import datetime

# -----------------------------
# Initialize Webcam
# -----------------------------
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Unable to access webcam.")
    exit()

print("Loading known faces...")

known_face_encodings = []
known_face_names = []

# -----------------------------
# Load Images and Create Encodings
# -----------------------------
image_folder = "images"

if not os.path.exists(image_folder):
    print("Images folder not found.")
    exit()

for file in os.listdir(image_folder):
    if file.endswith(".jpg"):
        image_path = os.path.join(image_folder, file)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            known_face_encodings.append(encodings[0])
            name = os.path.splitext(file)[0]
            known_face_names.append(name)

students = known_face_names.copy()

# -----------------------------
# Create Attendance File
# -----------------------------
date_today = datetime.now().strftime("%d-%m-%Y")
attendance_folder = "attendance_records"

if not os.path.exists(attendance_folder):
    os.makedirs(attendance_folder)

file_path = os.path.join(attendance_folder, f"{date_today}.csv")

f = open(file_path, "a+", newline="")
writer = csv.writer(f)

print("Attendance system started. Press 'q' to quit.")

# -----------------------------
# Main Loop
# -----------------------------
while True:
    ret, frame = video_capture.read()

    if not ret:
        print("Failed to capture frame.")
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

        name = "Unknown"

        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        if name != "Unknown":
            cv2.putText(frame, f"{name} Present",
                        (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2)

            if name in students:
                students.remove(name)
                current_time = datetime.now().strftime("%H:%M:%S")
                writer.writerow([name, current_time])
                print(f"{name} marked present at {current_time}")

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()