# Face Recognition Attendance System

## Overview

This project was built to automate the traditional attendance marking process using facial recognition. 
The goal was to minimize manual errors and create a lightweight system that can identify individuals in real-time using a webcam feed.

Instead of relying on manual roll calls or RFID systems, this solution uses computer vision techniques to detect and recognize faces and mark attendance automatically.

## Why This Project?

Manual attendance tracking can be time-consuming and error-prone, especially in classrooms or small organizations. I wanted to explore how computer vision could be used to simplify this process while keeping the system efficient and easy to deploy.

## Features

- Real-time face detection using webcam
- Face encoding and matching
- Automatic attendance logging
- Duplicate entry prevention
- Timestamp recording
- Simple and lightweight setup

## Tech Stack

- Python
- OpenCV
- face_recognition library
- NumPy
- Pandas

## How It Works

1. Images of individuals are stored and encoded.
2. The system captures real-time video from the webcam.
3. Detected faces are compared against stored encodings.
4. If a match is found, attendance is recorded with a timestamp.
5. The system ensures that attendance for the same person is not marked multiple times in one session.

## Installation

```bash
pip install -r requirements.txt
