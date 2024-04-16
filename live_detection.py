import cv2
import itertools
import numpy as np
from time import time
import os
import json
import mediapipe as mp
import matplotlib.pyplot as plt

# Initialize the mediapipe face detection class.
mp_face_detection = mp.solutions.face_detection


face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

# Initialize the mediapipe drawing class.
mp_drawing = mp.solutions.drawing_utils

# Initialize the mediapipe face mesh class.
mp_face_mesh = mp.solutions.face_mesh

# Setup the face landmarks function for images.
face_mesh_images = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=2,
                                         min_detection_confidence=0.5)

# Setup the face landmarks function for videos.K
face_mesh_videos = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1,
                                         min_detection_confidence=0.5, min_tracking_confidence=0.3)

# Initialize the mediapipe drawing styles class.
mp_drawing_styles = mp.solutions.drawing_styles

# Initialize the VideoCapture object to read from the webcam.
camera_video = cv2.VideoCapture(0)
camera_video.set(3, 1280)
camera_video.set(4, 960)


# Create named window for resizing purposes.
cv2.namedWindow('Face Landmarks Detection', cv2.WINDOW_NORMAL)

# Initialize a variable to store the time of the previous frame.
time1 = 0

#Read the first frame.
ok, frame = camera_video.read()
if not ok:
    exit("Cannot read the first frame")

# Perform Face landmarks detection on the first frame.
face_mesh_results = face_mesh_videos.process(frame)
#count = 0

# Check if facial landmarks are found.
if face_mesh_results.multi_face_landmarks:
    # Extract the first detected face landmarks.
    final_values = []
    face_landmarks = face_mesh_results.multi_face_landmarks[0]
    # Iterate over the landmarks and print x, y, and z coordinates.
    # print(face_landmarks)
    for landmark in face_landmarks.landmark:
        #count += 1
        #print(landmark)
        x = landmark.x
        y = landmark.y
        z = landmark.z
        #final_values.append(x,y,z)
        #print(count)
        # v=f"x: {x}, y: {y}, z: {z}"
        final_values.append(

                {
            #: count +0,
            "x":x,
            "y": y,
            "z": z
        }

        )

    final_values = [[final_values]]
    folder_path = 'C:/Users/user/PycharmProjects/goldebn ratio/PycharmProjects/pythonProject'
    #with open("input_1.json", 'w') as f:
    output = 'input_1.json'
    with open(os.path.join(folder_path, output), 'w') as output:
            json.dump(final_values, output,indent=2)



else:
    print("\033[32mNO FACE DETECTED\033[0m")



cv2.imwrite('inputimage.jpg',frame)
# Display the first frame.
cv2.imshow('Face Landmarks Detection', frame)
cv2.waitKey(0)
# Release the VideoCapture Object and close the windows.
camera_video.release()
cv2.destroyAllWindows()
