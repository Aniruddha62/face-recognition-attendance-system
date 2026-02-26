# Face Recognition Attendance System

## Overview

This project is a real-time face recognition based attendance system built using Python and OpenCV. 
It captures live video from a webcam, detects faces, and automatically marks attendance by matching them with stored images.

The main objective was to explore practical applications of computer vision in automating manual attendance processes.

## Features

- Real-time face detection
- Face encoding and comparison
- Automatic attendance marking
- Timestamp recording
- Duplicate entry prevention
- Automatic daily CSV file generation

## Project Structure

images/  
attendance_records/  
main.py  
requirements.txt  

## How It Works

1. Store images of individuals inside the `images/` folder.
2. The system encodes each face.
3. Live webcam feed detects faces in real time.
4. If a match is found, attendance is recorded.
5. A CSV file is created for each day.

Press `q` to exit.

## Future Improvements

- Integration with a database
- Web-based dashboard
- Improved recognition accuracy handling

## 👨‍💻 Author

**ANIRUDDHA BHATTACHARYYA**
