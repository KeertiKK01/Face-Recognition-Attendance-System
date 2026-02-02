# Face Recognition Attendance System

## 📖 Overview
The Face Recognition Attendance System is a Python-based application that uses Computer Vision and Machine Learning techniques to automatically detect and recognize faces through a webcam and store attendance records in a MySQL database.  
This system eliminates manual attendance and provides a secure, fast, and accurate attendance process.

---

## ✨ Features
- Real-time face detection and recognition
- Automatic attendance marking
- MySQL database integration
- Daily auto table creation for attendance
- Duplicate entry prevention
- Easy to use interface
- Fast and accurate recognition

---

## 🛠️ Technologies Used
- **Python**
- **OpenCV (cv2)**
- **face_recognition Library**
- **NumPy**
- **MySQL**
- **OS & Datetime Modules**

---

## 📂 Project Structure
Face-Recognition-Attendance-System/
│
├── Photos/ # Folder containing student images
│ ├── John.jpg
│ ├── Alice.jpg
│ └── ...
│
├── main.py # Main program file
├── requirements.txt # Python dependencies
├── database.sql # (Optional) DB schema
└── README.md # Project documentation

## ▶️ How to Run
1. Add student photos inside the **Photos** folder.  
   (File name = Student Name)
2. Connect your webcam.
3. Run the program:
4. Press **Q** to exit.

## 🧠 How It Works
- Loads images from Photos folder.
- Encodes faces using face_recognition.
- Captures live webcam video.
- Matches detected faces with stored encodings.
- Marks attendance in MySQL with date & time.
- Creates a new table daily (attendance_YYYY_MM_DD).

## 🎯 Use Cases
- College Attendance
- Office Employee Tracking
- Secure Entry Systems
- Classroom Monitoring

## 📄 Output
- Recognizes faces in real time.
- Stores attendance records with name, date, and time.

## 👩‍💻 Author
Keerti Kushwaha
