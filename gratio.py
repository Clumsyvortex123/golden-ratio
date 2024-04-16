import math
import numpy as np
import cv2 as cv
import mediapipe as mp
from demo3 import bulge_values as fina_amt
from demo2 import bulge_values
from PIL import Image
#from live_detection import frame
from trial import image
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
# eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
f_img ='C:/Users/user/PycharmProjects/goldebn ratio/PycharmProjects/pythonProject/inputimage.jpg'
im_cv = cv.imread(f_img)
# faces = eye_cascade.detectMultiScale(im_cv, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
# print(faces)
(h, w, _) = im_cv.shape

scale_x = 1.0
scale_y = 1.0
radius = min(w, h) / 2
print("radius->", radius)

flex_x = np.zeros((h, w), np.float32)
flex_y = np.zeros((h, w), np.float32)
print("radius1->", flex_x)
print("radius2->", flex_y)
results = face_mesh.process(im_cv)
landmarks_data = {}
if results.multi_face_landmarks:
    my_list =fina_amt


#*****************************************************************************************************
        # {'l': 151, 'amount': 0.026262061500447745},
        # {'l': 168, 'amount': 0.04345980260124959},
        # {'l': 4, 'amount': 0.06688081249704575},
#nose-----------------------------------------------------------------------------------------
        # {'l': 195, 'amount': 0.1010392751701138403}, {'l': 168, 'amount': 0.012831363887473149},
        #  {'l': 151, 'amount': 0.017507213591643415},

#jaw butterfly centre------------------------------------------------------------------------------------------
        # {'l': 187, 'amount': 0.03445338705985562}, {'l': 207, 'amount': 0.013205664951241092},
        #  {'l': 216, 'amount': 0.008205218769172809}, {'l': 186, 'amount': 0.004471057102499183},
        #  {'l': 411, 'amount': 0.013185465930298193}, {'l': 427, 'amount': 0.012066394227651212},
        #  {'l': 436, 'amount': 0.006657363677077116}, {'l': 410, 'amount': 0.003477435697479915},


#forehead-------------------------------------------------------------------------------------
        # {'l': 67, 'amount': 0.00937439242714578}, {'l': 109, 'amount': 0.010742230593592708},
        #  {'l': 10, 'amount': 0.1011664524030585051}, {'l': 338, 'amount': 0.010763837603332473},
        #  {'l': 297, 'amount': 0.008835504738285468},
#upper_jaw------------------------------------------------------------------------------------
        # {'l': 117, 'amount': 0.008229916251574793}, {'l': 118, 'amount': 0.008772067487599525},
        #  {'l': 101, 'amount': 0.010520799217713844}, {'l': 36, 'amount': 0.007893379641114171},
        #  {'l': 203, 'amount': 0.007627039181475798}, {'l': 165, 'amount': 0.009813753837026672},
        #  {'l': 39, 'amount': 0.004729085109531277}, {'l': 391, 'amount': 0.006968808923837704},
        #  {'l': 423, 'amount': 0.012112036107696275}, {'l': 266, 'amount': 0.008711517312276942},
        #  {'l': 330, 'amount': 0.008701429081118983}, {'l': 347, 'amount': 0.013073272787574947},
        #  {'l': 346, 'amount': 0.008889492511365175}, {'l': 340, 'amount': 0.008711872803225024},
#jaw_curve between nose and lip
        # {'l': 207, 'amount': 0.017809587620280398}, {'l': 427, 'amount': 0.023631883060271447},
#jaw_nose_curve
        # {'l': 205, 'amount': 0.011570871656413906}, {'l': 207, 'amount': 0.011528286174164064},
        #  {'l': 214, 'amount': 0.011791219946955013}, {'l': 135, 'amount': 0.011365222813363697},
        #  {'l': 425, 'amount': 0.012678383752225672}, {'l': 427, 'amount': 0.012148234068193979},
        #  {'l': 434, 'amount': 0.012306682871369497}, {'l': 364, 'amount': 0.011993194089512618}

#*****************************************************************************************************
#]
    for element in my_list:
        landmark_index = element['l']
        #print(landmark_index)
        amount = element['amount']
        landmark_point = results.multi_face_landmarks[0].landmark[landmark_index]

        center_x = int(landmark_point.x * im_cv.shape[1])
        center_y = int(landmark_point.y * im_cv.shape[0])

        for y in range(h):
            delta_y = scale_y * (y - center_y)
            for x in range(w):
                delta_x = scale_x * (x - center_x)
                distance = delta_x * delta_x + delta_y * delta_y
                if distance >= (radius * radius):
                    flex_x[y, x] = x
                    flex_y[y, x] = y
                else:
                    factor = 1.0
                    if distance > 0.0:
                        factor = math.pow(math.sin(math.pi * math.sqrt(distance) / radius / 2), -amount)
                    flex_x[y, x] = factor * delta_x / scale_x + center_x
                    flex_y[y, x] = factor * delta_y / scale_y + center_y

        dst = cv.remap(im_cv, flex_x, flex_y, cv.INTER_LINEAR)
        im_cv = dst
output_file = 'modified_image.jpg'
        # cv.imshow('input_image',frame)
in_img = 'C:/Users/user/PycharmProjects/goldebn ratio/PycharmProjects/pythonProject/inputimage.jpg'
a = cv.imread(in_img)
input=cv.imshow('input_image', a)
cv.imwrite(output_file, dst)
output=cv.imshow('C:/Users/user/PycharmProjects/goldebn ratio/PycharmProjects/pythonProject/output_image', dst)
cv.waitKey(0)
fil=cv.imshow("Filtered Image", image)
cv.waitKey(0)
cv.destroyAllWindows()



