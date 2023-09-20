import numpy as np
import mediapipe as mp
import cv2


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)

mphands = mp.solutions.hands
hands = mphands.Hands(min_detection_confidence=0.9)
mpdraw = mp.solutions.drawing_utils

Paint = cv2.imread('Paint.png')
Pen = cv2.imread('Pen.png')

blank = np.ones((720, 1280, 3), np.uint8) * 255



color = (0, 0, 0)
obj = 'pen'
finger_up = False
finger_position = None

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
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
            
    if len(lm_list) != 0:
        x1, y1 = lm_list[8][1:]
        x2, y2 = lm_list[12][1:]
        
        finger1 = lm_list[8][2] < lm_list[8 - 2][2]
        finger2 = lm_list[12][2] < lm_list[12 - 2][2]
            
        if finger1 and finger2:
            x_line, y_line = 0, 0
            if x1 > 0 and y1 < 125:
                if 0 < x1 < 183:
                    color = (0, 0, 0)
                elif 183 < x1 < 366:
                    color = (255, 0, 0)
                elif 366 < x1 < 549:
                    color = (0, 0, 255)
                elif 549 < x1 < 732:
                    color = (0, 255, 0)
                elif 732 < x1 < 915:
                    obj = 'circle'
                elif 915 < x1 < 1098:
                    obj = 'rectangle'
                elif 1098 < x1 < 1280:
                    obj = 'eraser'
                    color = (255, 255, 255)

            elif x1 > 1160 and y1 > 125:
                obj = 'pen'

            if obj == 'rectangle' and finger_up:
                cv2.rectangle(blank, finger_position, point2, color, 2)

            if obj == 'circle' and finger_up:
                cv2.circle(blank, finger_position, int(((finger_position[0]-point2[0])**2 + (finger_position[1]-point2[1])**2)**0.5), color, 2)
         
        if obj == 'rectangle' and finger_up:
            if color != (255, 255, 255):
                cv2.rectangle(frame, finger_position, (x1, y1), color, 2)

        if obj == 'circle' and finger_up:
            if color != (255, 255, 255):
                cv2.circle(frame, finger_position, int(((finger_position[0]-point2[0])**2 + (finger_position[1]-point2[1])**2)**0.5), color, 2)
        
        if finger1 and not finger2 and not finger_up:
            finger_position = (x1, y1)
            finger_up = True
            
        elif finger1 and finger2:
            finger_up = False
            
        if finger1 and finger2 == False:
            if x_line == 0 and y_line == 0:
                x, y = x1, y1
            if obj == 'eraser' and color == (255, 255, 255):
                cv2.circle(blank, (x1, y1), 50, color, -1)
                cv2.circle(frame, (x1, y1), 50, color, -1)
            elif obj == 'pen':
                cv2.line(blank, (x_line, y_line), (x1, y1), color, 10)
                
            point2 = (x1, y1)
            
        x_line, y_line = x1, y1
            
    frame = cv2.bitwise_and(frame, blank)
    frame[0:120, 0:1280] = Paint
    frame[120:, 1160:] = Pen
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()