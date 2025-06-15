# CodeAlpha_Object_Detection
Object Detection using YOLOv8 - CodeAlpha Internship
# CodeAlpha\_Object\_Detection

=Object Detection and Tracking using YOLOv8

This project is submitted as part of the CodeAlpha Internship. The goal was to build a real-time object detection system using deep learning models. I chose to work with YOLOv8 for its speed and accuracy.

------------------------------------------------------

=Project Description

This Python-based project performs real-time object detection using a pretrained **YOLOv8n** model via the `ultralytics` library. It utilizes OpenCV for video streaming and visualization.

=Key Features:

* Detects and classifies objects in real-time from webcam or video file.
* Draws bounding boxes around detected objects.
* Press `q` to quit the live detection.

------------------------------------------------------

=Technologies Used

* Python 3.10+
* [YOLOv8](https://github.com/ultralytics/ultralytics)
* OpenCV
* Ultralytics library

------------------------------------------------------

=How to Run the Project

1. Clone the repo**:

   ```bash
   git clone https://github.com/SandyAntonius/CodeAlpha_Object_Detection.git
   cd CodeAlpha_Object_Detection
   ```

2. Install requirements**:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the detection**:

   ```bash
   python object_detection.py
   ```

   > Note: If webcam is not available, replace:

   ```python
   video_source = 0
   ```

   with:

   ```python
   video_source = "your_video.mp4"
   ```

------------------------------------------------------

=Demo Video

> A short video demo has been shared in the LinkedIn submission post.

---

=Output Example

When you run the script, you will see a window showing the live video with bounding boxes around detected objects like:

* person
* car
* bag
* cell phone

------------------------------------------------------

=Created by

Sandy Antonius
CodeAlpha Intern - June 2025

------------------------------------------------------
=Connect with Me:

- GitHub: [github.com/SandyAntonius](https://github.com/SandyAntonius)
- LinkedIn: [linkedin.com/in/sandy-antonius-6627652a7](https://www.linkedin.com/in/sandy-antonius-6627652a7)
------------------------------------------------------

> Special thanks to CodeAlpha for the opportunity to work on real-world AI projects!
