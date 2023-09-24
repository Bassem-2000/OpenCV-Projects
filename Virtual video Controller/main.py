import cv2
import mediapipe as mp
import pyautogui as p
import time
import webbrowser
import pygetwindow as gw
import argparse

# Initialize MediaPipe Hands
mphands = mp.solutions.hands
hands = mphands.Hands(min_detection_confidence=0.9)
mpdraw = mp.solutions.drawing_utils

# Function to activate a specific window
def activate_window(window_title):
    target_window = gw.getWindowsWithTitle(window_title)
    if target_window:
        target_window[0].activate()

def main(video_path):
    # Set the video capture properties
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 120)

    # Open the video in the default web browser
    webbrowser.open(video_path)

    # Initialize variables for hand gestures
    closed_hands_time = None
    full_window = None
    prev_time = None
    forward_time = None
    vol_up = None
    vol_down = None
    stop = None

    while True:
        ret, frame = cap.read()

        # Flip the frame horizontally for a mirrored view
        frame = cv2.flip(frame, 1)

        # Convert the frame to RGB format for Mediapipe
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        lm_list = []

        if results.multi_hand_landmarks:
            for handlm in results.multi_hand_landmarks:
                for id, lm in enumerate(handlm.landmark):
                    h, w, c = frame.shape
                    x, y = int(lm.x * w), int(lm.y * h)
                    lm_list.append([id, x, y])
                mpdraw.draw_landmarks(frame, handlm, mphands.HAND_CONNECTIONS)

        # Detect hand gestures
        finger1 = False
        finger2 = False
        finger3 = False
        finger4 = False

        if len(lm_list) != 0:
            finger0_xy_3 = lm_list[3][1:]
            finger1_up = lm_list[8][2] < lm_list[6][2]
            finger2_up = lm_list[12][2] < lm_list[10][2]
            finger0_xy = lm_list[4][1:]
            finger1_xy = lm_list[8][1:]
            finger4_xy = lm_list[20][1:]

            finger0 = lm_list[4][2] < lm_list[2][2]
            finger1 = lm_list[8][2] > lm_list[6][2]
            finger2 = lm_list[12][2] > lm_list[10][2]
            finger3 = lm_list[16][2] > lm_list[14][2]
            finger4 = lm_list[20][2] > lm_list[18][2]
            
            # Check for the 'F11' gesture
            if (abs(finger0_xy[0] - finger1_xy[0]) <= 25) and (abs(finger0_xy[1] - finger1_xy[1]) <= 25):
                forward_time = None
                closed_hands_time = None
                prev_time = None
                vol_down =  None
                vol_up = None

                if full_window is None:
                    full_window = time.time()
                elif time.time() - full_window >= 0.5: 
                    activate_window('Media Player')
                    p.press('f11')
                    full_window = time.time()      
            
            # Check for the 'Ctrl+Left' gesture
            elif (finger0_xy[0] < finger4_xy[0]) and (finger0_xy[0] < finger0_xy_3[0]) and finger1 and finger2 and finger3 and finger4:
                forward_time = None
                closed_hands_time = None
                full_window = None
                vol_down =  None
                vol_up = None

                if prev_time is None:
                    prev_time = time.time()
                elif time.time() - prev_time >= 0.5: 
                    activate_window('Media Player')
                    p.hotkey('ctrl', 'left')
                    prev_time = time.time() 
            
            # Check for the 'Ctrl+Right' gesture
            elif (finger0_xy[0] > finger4_xy[0]) and (finger0_xy[0] > finger0_xy_3[0]) and finger1 and finger2 and finger3 and finger4:
                closed_hands_time = None
                full_window = None
                prev_time = None
                vol_down =  None
                vol_up = None

                if forward_time is None:
                    forward_time = time.time()
                elif time.time() - forward_time >= 0.5: 
                    activate_window('Media Player')
                    p.hotkey('ctrl', 'right')
                    forward_time = time.time()   
            
            # Check for the 'Space' gesture
            elif finger0 and finger1 and finger2 and finger3 and finger4:
                full_window = None
                prev_time = None
                vol_down =  None
                vol_up = None
                forward_time = None

                if closed_hands_time is None:
                    closed_hands_time = time.time()
                elif time.time() - closed_hands_time >= 0.5: 
                    activate_window('Media Player')
                    p.press('space')
                    closed_hands_time = time.time()   
            
            # Check for the 'Volume Up' gesture
            elif finger1_up and finger2 and finger3 and finger4:
                forward_time = None
                closed_hands_time = None
                full_window = None
                prev_time = None
                vol_down =  None

                if vol_up is None:
                    vol_up = time.time()
                elif time.time() - vol_up >= 0.5: 
                    activate_window('Media Player')
                    p.press('volumeup')
                    vol_up = time.time()  
            
            # Check for the 'Volume Down' gesture
            elif finger1_up and finger2_up and finger3 and finger4:
                forward_time = None
                closed_hands_time = None
                full_window = None
                prev_time = None
                vol_up = None

                if vol_down is None:
                    vol_down = time.time()
                elif time.time() - vol_down >= 0.5: 
                    activate_window('Media Player')
                    p.press('volumedown')
                    vol_down = time.time()  
            else:
                forward_time = None
                closed_hands_time = None
                full_window = None
                prev_time = None
                vol_down =  None
                vol_up = None

        cv2.imshow('Video', frame)
        
        # Detect the gesture to stop the video
        if not (finger1) and not (finger4) and finger2 and finger3:
            if stop is None:
                stop = time.time()
            elif time.time() - stop >= 0.5: 
                activate_window('Media Player')
                p.hotkey('alt', 'f4')
                break  
        cv2.waitKey(1)

    # Release the video capture and close all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Control video playback using hand gestures')
    parser.add_argument('video_path', type=str, help='Path to the video file')
    args = parser.parse_args()

    main(args.video_path)
