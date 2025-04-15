import json   
import os
from tqdm import tqdm

f=open(r"E:\Datasets\xray\Segmentation\teeth_polygon.json")
save_path = r"E:\Datasets\xray\Segmentation\json_files"
os.makedirs(save_path, exist_ok=True)
test=json.load(f)
for obj in tqdm(test):
    filename = os.path.join(save_path, str(obj['External ID'].replace('.jpg', '.json')))
    with open(filename, 'w') as f:
        json.dump(obj, f)