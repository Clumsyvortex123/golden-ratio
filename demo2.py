import json
import os
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2

from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np

import cv2 as cv
import matplotlib.pyplot as plt
# from google.colab.patches import cv2_imshow
'''def plot_face_blendshapes_bar_graph(face_blendshapes):
# Extract the face blendshapes category names and scores.
  face_blendshapes_names = [face_blendshapes_category.category_name for face_blendshapes_category in face_blendshapes]
  face_blendshapes_scores = [face_blendshapes_category.score for face_blendshapes_category in face_blendshapes]
# The blendshapes are ordered in decreasing score value.
  face_blendshapes_ranks = range(len(face_blendshapes_names))
  fig, ax = plt.subplots(figsize=(12, 12))
  bar = ax.barh(face_blendshapes_ranks, face_blendshapes_scores,
  label=[str(x) for x in face_blendshapes_ranks])
  ax.set_yticks(face_blendshapes_ranks, face_blendshapes_names)
  ax.invert_yaxis()
# Label each bar with values
  for score, patch in zip(face_blendshapes_scores, bar.patches):
      plt.text(patch.get_x() + patch.get_width(), patch.get_y(),f"{score:.4f}", va="top")
  ax.set_xlabel('Score')
  ax.set_title("Face Blendshapes")
  plt.tight_layout()
# plt.show()
# STEP 2: Create an FaceLandmarker object.
base_options = python.BaseOptions(model_asset_path='C:/Users/Employee/Downloads/face_landmarker.task')
options = vision.FaceLandmarkerOptions(base_options=base_options,
output_face_blendshapes=True,
output_facial_transformation_matrixes=True,
num_faces=1)
detector = vision.FaceLandmarker.create_from_options(options)
# STEP 3: Load the input image.
img = cv2.imread("C:/Users/Employee/PycharmProjects/pythonProject/golden ratio/kavya.jpg")
image = mp.Image.create_from_file("C:/Users/Employee/PycharmProjects/pythonProject/golden ratio/kavya.jpg")
# STEP 4: Detect face landmarks from the input image.
detection_result = detector.detect(image)
# print(detection_result.face_landmarks)
# print(detection_result.face_blendshapes)
plot_face_blendshapes_bar_graph(detection_result.face_blendshapes[0])
# print("val->",detection_result.facial_transformation_matrixes)
# print("val->",detection_result.face_landmarks)
val = detection_result.face_landmarks
no =0
print(len(val))
output_data = [[],[]]
# output_data[0] = [
# [
# {"x": float(item.x), "y": float(item.y), "z": item.z,"visibility": item.visibility,"presence":item.presence}
# for item in category_list
# ]
# for category_list in detection_result.face_landmarks
# ]
output_data[0] = [
[
{
#"index": index + 1, # Adding index value starting from 1
"x": float(item.x),
"y": float(item.y),
"z": item.z,
#"visibility": item.visibility,
#"presence": item.presence,
}
for index, item in enumerate(category_list)
]
for no, category_list in enumerate(detection_result.face_landmarks)
]
# output_data[1] = [
# [
# {"index": item.index, "score": str(item.score), "display_name":
# item.display_name, "category_name": item.category_name}
# for item in category_list
# ]
# for category_list in detection_result.face_blendshapes
# ]
# json_object.append(json_data)
# print(output_data)
json_formatted_str = json.dumps(output_data, indent=2)
with open('C:/Users/Employee/PycharmProjects/pythonProject/sample.json','w') as json_file:
 json_file.write(json_formatted_str)'''

folder_path = 'C:/Users/user/PycharmProjects/goldebn ratio/PycharmProjects/pythonProject'
json_name = 'input_1.json'
with open(os.path.join(folder_path, json_name), 'r') as jsonfile:
  json_data = json.load(jsonfile)
  filter_landmark = [
#--------------------------------------
# #upper jaw left//
       {
          'start':111 ,
          'end':117
      },
      {

          'start': 118,
          'end':101
      },
      {
          'start':36 ,
          'end':203
      },
      {

          'start':165,
          'end':39
      },
  #upper jaw right
      {

          'start':340,
          'end':346
      },
      {
          'start':347 ,
          'end':330
      },
      {

          'start':266 ,
          'end':423
      },
      {
          'start':391,
      'end':269
   },
#-----------------------------------------------------
#

#reverse nose//
     # #
     #  {
     #      'start':151,
     #  'end':8
     #  },
     #  {
     #    'start':168,
     #    'end':197
     # },
     #  {
     #      'start':195,
     #  'end':4
     #  },
  {
      'start':4,
      'end':195
  },
  {
      'start':197,
       'end':168
  },

  {
      'start':8,
  'end':151
  },

#jaw-----------------------------------------------------------//
  # {
  #     'start': 215,
  #     'end':187
  # },
  #
  # {
  #     'start':136,
  #     'end':214
  # },
  #
  # {
  #     'start': 150,
  #     'end':210
  # },
  #
  # {
  #     'start': 435,
  #     'end':411
  # },
  #
  # {
  #     'start':365 ,
  #     'end':434
  # },
  #
  # {
  #     'start':379,
  #     'end': 430
  # },


#eyebrows
  # {
  #     'start':55 ,
  #     'end':108
  # },
  # {
  #     'start':285,
  # 'end':337
  # },



# jaw butterfly / line//
#       {
#           'start':123,
#            'end':117
#       },
#       {
#           'start':187,
#       'end':118
#       },
#        {
#           'start':207,
#        'end':101
#        },
#       {
#           'start':216,
#       'end':203
#       },
#       {
#           'start':186,
#       'end':165
#       },
#       {
#           'start':352,
#            'end':346
#       },
#       {
#           'start':411,
#       'end':347
#       },
#        {
#           'start':427,
#        'end':330
#        },
#       {
#           'start':436,
#       'end':423
#       },
#       {
#           'start':410,
#       'end':391
#       },

#small jaw---------------------------------------------------------
# {
#
#           'start':138,
#           'end':187
#
#       },
#        {
#           'start':135,
#           'end':207
#       },
#       {
#
#           'start':367,
#           'end':411
#
#        },
#
#       {
#
#           'start':364,
#           'end':427
#
#        },
#-------------------------------------------------------------
  #     {
  #     'start':169,
  # 'end':207
  #
  # },
  # {
  #     'start':379,
  # 'end':427
  # },

#curve jaw--------------------------------------------------------------.//
# {
#     'start':101,
#     'end':36
# },
# {
#       'start':50,
#      'end':205
#
#   },
#   {
#       'start':187,
#   'end':207
#   },
# {
#         'start':192,
#         'end':214
#         },
# {
#       'start':138,
#  'end':135
# },
# {
#       'start':172 ,
#        'end':136
# },
#       {
#       'start':330,
#       'end':266
# },
#   {
#       'start':280,
#       'end':425
#   },
#   {
#       'start':411,
#      'end':427
#   },
#   {
#       'start':416,
#   'end':434
#   },
#   {
#       'start':367,
#   'end':364
#   },
#   {
#       'start':397,
#   'end':365
#   },
# #-----------------------------------------------------------------------
# #big jaw
# {
#             'start':40,
#         'end':92
#         },
#   {
#       'start':206,
#   'end':205
#   },
#   {
#       'start':50,
#   'end':123
#   },
#   {
#       'start':116,
#   'end':143
#   },{
#             'start':270,
#         'end':322
#         },{
#             'start':426,
#         'end':425
#         },{
#             'start':280,
#         'end':352
#         },{
#             'start':345,
#         'end':372
#          },

#jaw butterfly outer line
      # {
      #       'start':186,
      #   'end':216
      #   },
      # {
      #     'start':207,
      # 'end':187
      # },
      # {
      #     'start':123,
      # 'end':117
      # },
      # {
      #     'start':118,
      # 'end':101
      # },
      # {
      #     'start':36,
      # 'end':203
      # },
      # {
      #     'start':165,
      # 'end':39
      # },
      # {
      #     'start':410,
      # 'end':436
      # },
      # {
      #     'start':427,
      # 'end':411
      # },
      # {
      #     'start':352,
      # 'end':346
      # },
      # {
      #     'start':347,
      #
      # 'end':330
      # },
      # {
      #     'start':266,
      # 'end':423
      # },
      # {
      #     'start':391,
      # 'end':269
      # },
#------------------------------------------------------------


  #center nose
      {'start':49,'end':45 },
      {'start':279,'end':275},


# forehead--------------------------------------------------//
#
#             {
#                 'start':67 ,
#                 'end':66
#             },
#             {
#                 'start':109 ,
#                 'end':107
#             },
#         {
#                 'start':10 ,
#                 'end':9
#             },
#             {
#                 'start':338 ,
#                 'end':336
#             },
        # {
        #         'start':297 ,
        #         'end': 296
        #     },
#---------------------------------------------------
      # {
      #     'start':8,
      # 'end':67
      # },
      # {
      #     'start':8,
      # 'end':297
      # },
#--------------------------------------

#chin1
      {
          'start':176,
      'end':182
      },
      {
          'start':148,
      'end':83
      },
      {
          'start':152,
      'end':18
      },
      {
          'start':377,
      'end':313
      },
      {
          'start':400,
      'end':406
      },
#chin2
      # {
      #     'start':32,
      # 'end':176
      # },
      # {
      #     'start':201,
      # 'end':148
      # },
      # {
      #     'start':200,
      # 'end':152
      # },
      # {
      #     'start':421,
      # 'end':377
      # },
      # {
      #     'start':262,
      # 'end':400
      # },

#chin3
      # {
      #     'start':148,
      # 'end':208
      # },
      # {
      #     'start':152,
      # 'end':200
      # },
      # {
      #     'start':377,
      # 'end':428
      # },
      # {
      #     'start':,
      # 'end':
      # },

  ]
  bulge_values =[]
  landmark_incides=[]
for item in json_data[0]:
 for landmark in filter_landmark:
    id_value = item[landmark['start']]
    id_value1 = item[landmark['end']]
    landmark1 = (id_value['x'],id_value['y'],id_value['z'])
    landmark2 = (id_value1['x'],id_value1['y'],id_value1['z'])
    distance1 = np.linalg.norm(np.array(landmark2)-np.array(landmark1))
    values =distance1

    bulge_values.append(values)
 print(bulge_values)

#print(id_value1)
with open("iamt.json" ,'w') as f:
    f.write(f"{bulge_values}")
# Initialize MediaPipe face detection and landmark estimation



#Initialize MediaPipe face detection and landmark estimation







