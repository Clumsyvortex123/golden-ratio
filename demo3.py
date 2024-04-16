
import json
import os
import numpy as np
from demo1 import bulge_values as r
from demo2 import bulge_values as n
from  demo2 import filter_landmark as f


filter_landmark = f
#[
#
#     {
#         'start': 150,
#         'end': 169
#     },
#
#     {
#         'start': 214,
#         'end': 187
#     },
#
#     {
#         'start': 123,
#         'end': 137
#     },
#
#     {
#         'start': 379,
#         'end': 394
#     },
#
#     {
#         'start': 434,
#         'end': 411
#     },
#
#     {
#         'start': 352,
#         'end': 323
#     },

#]
bulge_values = []

for landmark, i, j in zip(filter_landmark,n, r):

     a = abs(i-j)
     values = {'l':landmark['end'],'amount':a}
     bulge_values.append(values)
print(bulge_values)

with open("final_amt.json", 'w') as f:
    f.write(f"{bulge_values}")

