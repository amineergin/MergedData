import os
import json
from glob import glob
from os.path import basename
import numpy as np
from torchvision.io import read_image
from torchvision.ops import masks_to_boxes
from tqdm import tqdm

if __name__ == "__main__":

    organ = 'lungs'
    mask_paths = glob(rf"C:/Users/amine/.spyder-py3/KeypointsDetection/{organ}/*.png")
    save_path =  f"C:/Users/amine/.spyder-py3/KeypointsDetection/Annotations/{organ}"
    path_to_json_Lungs = "C:/Users/amine/.spyder-py3/KeypointsDetection/Annotations/lungs"
    json_files_Lungs = [pos_json for pos_json in os.listdir(path_to_json_Lungs) if pos_json.endswith('.json')]

    path_to_json_Heart = "C:/Users/amine/.spyder-py3/KeypointsDetection/Annotations/heart"
    json_files_Heart = [pos_json for pos_json in os.listdir(path_to_json_Heart) if pos_json.endswith('.json')]
    
    for i in json_files_Lungs:
            merged_data_path = rf"C:/Users/amine/.spyder-py3/KeypointsDetection/Merged_data"
            
            d1 = open(path_to_json_Lungs + "/" + i)
            data1 = json.load(d1)
            d1.close()
            d2 = open(path_to_json_Heart + "/" + i)
            data2 = json.load(d2)
            d2.close()


            merged_bboxes = []
            merged_keypoints = []
            merged_bboxes = data1['bboxes'] + (data2['bboxes'])
            merged_keypoints = data1["keypoints"][0] + (data2["keypoints"][0])
            merged_num_keypoints = data1['num_keypoints'] + data2['num_keypoints']

            new_json_file = {
                "file_name": i,
                "category_id": 1,
                "bboxes": merged_bboxes,
                "keypoints": merged_keypoints,
                "num_keypoints": merged_num_keypoints
            }

            json_object = json.dumps(new_json_file, indent=4)
            fp = open(fr'{merged_data_path}/{i}', 'w')
            fp.write(json_object)