import json
import os
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
from  demo2 import filter_landmark as f
import cv2 as cv
import matplotlib.pyplot as plt
folder_path = 'C:/Users/user/PycharmProjects/goldebn ratio/PycharmProjects/pythonProject'
json_name = 'reference_image1.json'
with open(os.path.join(folder_path, json_name), 'r') as jsonfile:
  json_data = json.load(jsonfile)
  filter_landmark = f#[

  # {
  #     'start': 150,
  #     'end': 169
  # },
  #
  # {
  #     'start': 214,[0.07935533127967566, 0.08016012881039081]
  #     'end': 187
  # },
  #
  # {
  #     'start':123 ,
  #     'end': 137
  # },
  #
  # {
  #     'start': 379,
  #     'end': 394
  # },
  #
  # {
  #     'start': 434,
  #     'end': 411
  # },
  #
  # {
  #     'start':352 ,
  #     'end': 323
  # },
  #     {
  #         'start': 123,
  #         'end': 117
  #     }
  # {
  #     'start': 123,
  #     'end': 118
  # },
  # {
  #     'start': 352,
  #     'end': 347
  # }
  #]
  bulge_values =[]
for item in json_data[0]:
 for landmark in filter_landmark:
   #print(landmark['end'])
# print(item)
   id_value = item[landmark['start']]
   id_value1 = item[landmark['end']]
   landmark1 = (id_value['x'],id_value['y'],id_value['z'])
   landmark2 = (id_value1['x'],id_value1['y'],id_value1['z'])
   distance = np.linalg.norm(np.array(landmark2)-np.array(landmark1))
   #print("Distance between landmarks:", distance)
   values = distance
            #'l':landmark['end'], 'amount':distance

   bulge_values.append(values)
 print(bulge_values)
# print(id_value1)

with open("ramt.json" ,'w') as f:
    f.write(f"{bulge_values}")

