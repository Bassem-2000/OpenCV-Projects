
# Hand Gesture Video Control

<div align="center">
    <img src="https://github.com/Bassem-2000/OpenCV-Projects/blob/main/Virtual%20video%20Controller/Pic.gif?raw=true">
  </div>

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Additional Notes](#additional-notes)
- [Contributing](#Contributing)
- [Contact](#Contact)
- [Feedback](#Feedback)

## Introduction

This Python script allows you to control video playback using hand gestures captured by your webcam. You can perform various gestures to play/pause the video, adjust the volume, skip forward or backward, and even make the video fullscreen. The script uses the MediaPipe and OpenCV libraries to detect hand landmarks and interprets them as gestures to control a video player (e.g., VLC or Windows Media Player).

## Features

- **Gesture-Based Video Control**.
- **Video Player Activation**.
- **Seamless Integration with Web Browsing**.
- **Real-Time Video Preview**.
- **Adjustable Parameters**.
- **Gesture Sensitivity**.

## Requirements

Make sure you have the following libraries installed before running the project:

- `OpenCV (cv2)`
- `MediaPipe (mediapipe)`
- `PyAutoGUI (pyautogui)`
- `Webbrowser (webbrowser)`
- `PyGetWindow (pygetwindow)`

You can install these libraries using pip:

```bash
pip install opencv-python mediapipe pyautogui pygetwindow
```
## Usage

1. Download the script file main.py.
2. Open your terminal/command prompt and navigate to the directory where the script is saved.
3. Run the script with the path to your video file as an argument. For example:
```bash
   python main.py path_to_your_video.mp4
```
4. The script will open your default web Camera and play the video. You can then use hand gestures to control the video playback.
5. Use the following gestures to interact with the application:
    - **Fullscreen (F11):** Bring your thumb and index finger close together to make the video fullscreen.
    - **Seek Backward (Ctrl+Left Arrow):** Close your Hands while keeping your thumb Extended to the left. This gesture will seek the video backward.
    - **Seek Forward (Ctrl+Right Arrow):** Close your Hands while keeping your thumb Extended to the right. This gesture will seek the video forward.
    - **Play/Pause (Space):** Close your hand into a fist to play or pause the video.
    - **Volume Up (Volume Up Key):** Raise your index finger while keeping your other fingers closed to increase the volume.
    - **Volume Down (Volume Down Key):** Raise your index and middle fingers while keeping your other fingers closed to decrease the volume.
    - **Stop (Alt+F4):** Extend your index and pinky fingers while keeping your middle, thumb, and ring fingers closed. This gesture will stop the video and close the player.


## Additional Notes

If the script doesn't work as expected, ensure that your webcam is properly configured and that the required libraries are installed.
Note: This script is designed to work with specific hand gestures and may require adjustments or additional gestures to suit your preferences or the video player you are using.
Enjoy controlling your video playback with hand gestures!

## Contributing

Contributions to this project are welcome! If you have ideas for improvements or bug fixes, please create an issue or submit a pull request.

## Contact

[<img alt="alt_text" width="30px" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Whatsapp2_colored_svg-512.png" />](https://wa.me/+201006491306)
&nbsp;&nbsp;
[<img alt="alt_text" width="30px" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-512.png" />](https://www.linkedin.com/in/bassem-ahmed-ahmed/)
&nbsp;&nbsp;
[<img alt="alt_text" width="30px" src="https://cdn4.iconfinder.com/data/icons/social-media-logos-6/512/112-gmail_email_mail-256.png" />](mailto:bassemahmed.am@gmail.com) 
[<img alt="alt_text" width="30px" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Facebook2_colored_svg-512.png" />](https://www.facebook.com/bassem.ahmed.7712/)


## Feedback

Can you please provide me with feedback on how I can improve myself and any ideas to improve the model, I am eager to receive any advice that can help me develop my skills.

&nbsp;&nbsp;
**Wish you a nice day :)**
