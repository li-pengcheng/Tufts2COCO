import os,json,string
from tqdm import tqdm
import shutil

image_path = r'E:\Datasets\xray\Radiographs'
masks_path = r'E:\Datasets\xray\Segmentation\teeth_mask'
jsons_path = r'E:\Datasets\xray\Segmentation\json_files'

save_image_path = r'E:\Datasets\xray\Radiographs_morethan32'
save_masks_path = r'E:\Datasets\xray\Segmentation_morethan32'
save_jsons_path = r'E:\Datasets\xray\Json_morethan32'
os.makedirs(save_image_path,exist_ok=True)
os.makedirs(save_masks_path,exist_ok=True)
os.makedirs(save_jsons_path,exist_ok=True)

image_files = sorted(os.listdir(image_path))
mask_files = sorted(os.listdir(masks_path))
json_files = sorted(os.listdir(jsons_path))

for json_name in tqdm(json_files):
    json_path = os.path.join(jsons_path, json_name)
    with open(json_path, 'r') as f:
        data = json.load(f)
    f.close()
    for i, obj in enumerate(data["Label"]['objects']):
        title = obj['title']
        if title in [letter for letter in string.ascii_uppercase[:20]]:
            shutil.move(os.path.join(image_path, json_name.replace('.json', '.JPG')),
                        os.path.join(save_image_path,json_name.replace('.json', '.JPG')))
            shutil.move(os.path.join(masks_path, json_name.replace('.json', '.jpg')),
                        os.path.join(save_masks_path, json_name.replace('.json', '.jpg')))
            shutil.move(os.path.join(jsons_path, json_name),
                        os.path.join(save_jsons_path, json_name))
            break
