import os,shutil
from tqdm import tqdm
import json
import numpy as np

sourceDir="C:/Users/u7018195/Desktop/Hex-plane-continuation-DPM/lego/"

# spliting the full json file into 1st half and 2nd half
transforms_full1 = {"camera_angle_x":None, 'frames':[]}
transforms_full2 = {"camera_angle_x":None, 'frames':[]}

for root, _, files in os.walk(sourceDir):
    for file in files:
        if 'json' in file:
            with open(os.path.join(sourceDir,file), 'r', encoding='utf8') as fp:
                json_data = json.load(fp)
            transforms_full1["camera_angle_x"] = json_data["camera_angle_x"]
            transforms_full2["camera_angle_x"] = json_data["camera_angle_x"]
            frames = json_data['frames']
            length = len(frames)
            length1 = length // 2
            transforms_full1['frames'] += json_data['frames'][:length1]
            transforms_full2['frames'] += json_data['frames'][length1:]
            print(length, len(json_data['frames'][:length1]), len(json_data['frames'][length1:]))

dumps = json.dumps(transforms_full1)
f = open(sourceDir+'/transforms_full1.json', 'w')
f.write(dumps)
f.close()

dumps = json.dumps(transforms_full2)
f = open(sourceDir+'/transforms_full2.json', 'w')
f.write(dumps)
f.close()




