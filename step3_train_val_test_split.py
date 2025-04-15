import os
import shutil
import random

image_folder = r'E:\Datasets\xray\Radiographs'  # 图像文件夹路径
mask_folder = r'E:\Datasets\xray\Segmentation\teeth_mask'  # mask文件夹路径
json_folder = r'E:\Datasets\xray\Segmentation\json_files'  # json文件夹路径

# 获取所有图像文件的文件名（不包括文件扩展名）
image_filenames = [os.path.splitext(filename)[0] for filename in os.listdir(image_folder)]

# 计算每个文件夹应该包含的文件数量
train_files = 643
val_files = 91
test_files = 184

# 随机打乱文件名列表
random.shuffle(image_filenames)

# 遍历文件名列表，并将每个文件复制到相应的文件夹中
train_image_folder = r'E:\Datasets\xray\train\image'
val_image_folder = r'E:\Datasets\xray\val\image'
test_image_folder = r'E:\Datasets\xray\test\image'

train_mask_folder = r'E:\Datasets\xray\train\mask'
val_mask_folder = r'E:\Datasets\xray\val\mask'
test_mask_folder = r'E:\Datasets\xray\test\mask'

train_json_folder = r'E:\Datasets\xray\train\json'
val_json_folder = r'E:\Datasets\xray\val\json'
test_json_folder = r'E:\Datasets\xray\test\json'


os.makedirs(train_image_folder, exist_ok=True)
os.makedirs(val_image_folder, exist_ok=True)
os.makedirs(test_image_folder, exist_ok=True)
os.makedirs(train_mask_folder, exist_ok=True)
os.makedirs(val_mask_folder, exist_ok=True)
os.makedirs(test_mask_folder, exist_ok=True)
os.makedirs(train_json_folder, exist_ok=True)
os.makedirs(val_json_folder, exist_ok=True)
os.makedirs(test_json_folder, exist_ok=True)

files_copied = 0
for filename in image_filenames:
    image_path = os.path.join(image_folder, filename + '.jpg')
    mask_path = os.path.join(mask_folder, filename + '.jpg')
    json_path = os.path.join(json_folder, filename + '.json')

    if files_copied < train_files:
        shutil.move(image_path, train_image_folder)
        shutil.move(mask_path, train_mask_folder)
        shutil.move(json_path, train_json_folder)
    elif files_copied < train_files + val_files:
        shutil.move(image_path, val_image_folder)
        shutil.move(mask_path, val_mask_folder)
        shutil.move(json_path, val_json_folder)
    else:
        shutil.move(image_path, test_image_folder)
        shutil.move(mask_path, test_mask_folder)
        shutil.move(json_path, test_json_folder)

    files_copied += 1
