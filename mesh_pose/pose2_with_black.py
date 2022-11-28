import cv2
import mediapipe as mp
import numpy as np

cap=cv2.VideoCapture(0)

mp_pose=mp.solutions.pose
mpDraw=mp.solutions.drawing_utils
pose=mp_pose.Pose()


while True:
    
    ret,frame=cap.read()
    black = np.zeros(frame.shape).astype("uint8")
   
    flipped=cv2.flip(frame,flipCode=1)
    frame1 = cv2.resize(flipped,(640,480))
    rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
    result=pose.process(rgb_img)
    print (result.pose_landmarks)
    mpDraw.draw_landmarks(black,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
    cv2.imshow("frame",black)
    
    key = cv2.waitKey(1) & 0xFF
    if key ==ord("q"):
        break
        
