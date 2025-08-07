import face_recognition
import cv2
import numpy as np
import csv
import os
import mysql.connector
from datetime import datetime

# Database connection setup
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Keerti@kk01",
    database="facerecognition"
)
mycursor = mydb.cursor()

# Function to create a new table for attendance
def create_attendance_table(cursor, table_name):
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            time TIME NOT NULL,
            date DATE NOT NULL
        )
    """
    cursor.execute(create_table_query)

# Video capture setup
video_capture = cv2.VideoCapture(0)

# Directory containing photos
photos_directory = "Photos"

# Initialize lists to store encodings and names
known_face_encodings = []
known_face_names = []

# Iterate over photo files in the directory
for filename in os.listdir(photos_directory):
    photo_path = os.path.join(photos_directory, filename)
    name = os.path.splitext(filename)[0]  # Extract name from file name
    
    # Load image and encode it
    image = face_recognition.load_image_file(photo_path)
    encoding = face_recognition.face_encodings(image)[0]
    
    # Append encoding and name to lists
    known_face_encodings.append(encoding)
    known_face_names.append(name)

# Initialize variables for face recognition and attendance
students = known_face_names.copy()

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get current date
    current_date = datetime.now().strftime("%Y_%m_%d")
    table_name = f"attendance_{current_date}"

    # Check if table exists, if not, create it
    create_attendance_table(mycursor, table_name)

    # Face recognition logic...
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = ""
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            face_names.append(name)
            if name in students:
                students.remove(name)
                print(students)
                current_time = datetime.now().strftime("%H:%M")

                # Insert into MySQL
                sql = f"INSERT INTO {table_name} (name, time, date) VALUES (%s, %s, %s)"
                val = (name, current_time, current_date)
                mycursor.execute(sql, val)
                mydb.commit()  # Commit the transaction
            

    cv2.imshow("Attendance System", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
mydb.close() 