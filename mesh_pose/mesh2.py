import mediapipe as mp
import cv2
import numpy as np

def get_unique(c):
    temp_list = list(c)
    temp_set = set()
    for t in temp_list:
        temp_set.add(t[0])
        temp_set.add(t[1])
    return list(temp_set)


#img = cv2.VideoCapture(0)
img = cv2.imread("face1.jpg")
cap = cv2.VideoCapture(0)
if (cap.isOpened() == False): 
  print("Unable to read camera feed")    
  
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#img = cv2.resize(img, (600, 600))
#img.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#img.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
mp_face_mesh = mp.solutions.face_mesh

connections_irises = mp_face_mesh.FACEMESH_IRISES
irises_indices = get_unique(connections_irises)
connections_face_oval = mp_face_mesh.FACEMESH_FACE_OVAL
face_oval_indices = get_unique(connections_face_oval)

#black = np.zeros(img.shape).astype("uint8")

with mp_face_mesh.FaceMesh(
    static_image_mode = True,
    max_num_faces = 2,
    refine_landmarks = True,
    min_detection_confidence = 0.5) as face_mesh:
    while(cap.isOpened()):
        ret , frame = cap.read()
        if ret == False:
            break
        
        #annotated_image = img.copy()
        results = face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        for face_landmark in results.multi_face_landmarks:
            lms = face_landmark.landmark
            d = {}
            for index in face_oval_indices:
                x = int(lms[index].x * img.shape[1])
                y = int(lms[index].y * img.shape[0])
                d[index] = (x, y)
            black = np.zeros(img.shape).astype("uint8")
            for index in face_oval_indices:
                cv2.circle(black, (d[index][0], d[index][1]),
                           2, (0, 255, 0), -1)
            for conn in list(connections_face_oval):
                cv2.line(black,
                         (d[conn[0]][0] , d[conn[0]][1]),
                         (d[conn[1]][0] , d[conn[1]][1]),
                         (0, 0, 255) ,
                         1)
                      
            cv2.imshow("final", black)
            if cv2.waitKey(5) & 0xFF ==27:
                break
            
cap.release()
cv2.destroyAllWindows()