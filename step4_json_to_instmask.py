import os
import json
import cv2
import numpy as np
from tqdm import tqdm

masks_path = r'E:\Datasets\xray\Tufts_Dental_Dataset\train\mask'
jsons_path = r'E:\Datasets\xray\Tufts_Dental_Dataset\train\json'
save_path = r'E:\Datasets\xray\Tufts_Dental_Dataset\train\instmask'
os.makedirs(save_path,exist_ok=True)

mask_files = sorted(os.listdir(masks_path))
json_files = sorted(os.listdir(jsons_path))

def write_json_to_mask(json_path, mask_path, save_path):
    # Define a list of 32 RGB tuples with predefined values
    colors = {
        "1": (255, 0, 0), "2": (255, 106, 0), "3": (255, 216, 0), "4": (169, 255, 0),
        "5": (0, 255, 3), "6": (0, 255, 153), "7": (0, 242, 255), "8": (0, 61, 255),
        "9": (92, 0, 255), "10": (209, 0, 255), "11": (255, 0, 212), "12": (255, 0, 72),
        "13": (255, 73, 0), "14": (255, 179, 0), "15": (182, 255, 0), "16": (0, 255, 224),
        "17": (0, 142, 255), "18": (108, 0, 255), "19": (237, 0, 255), "20": (255, 0, 38),
        "21": (225, 200, 200), "22": (200, 200, 0), "23": (255, 129, 0), "24": (179, 0, 255),
        "25": (0, 255, 95), "26": (255, 0, 149), "27": (107, 0, 255), "28": (255, 229, 0),
        "29": (255, 74, 0), "30": (0, 255, 178), "31": (0, 206, 0), "32": (255, 0, 0),
        "A": (255, 0, 0), "B": (255, 106, 0), "C": (255, 216, 0), "D": (169, 255, 0),
        "E": (0, 255, 3), "F": (0, 255, 153), "G": (0, 242, 255), "H": (0, 61, 255),
        "I": (92, 0, 255), "J": (209, 0, 255), "K": (255, 0, 212), "L": (255, 0, 72),
        "M": (255, 73, 0), "N": (255, 179, 0), "O": (182, 255, 0), "P": (0, 255, 224),
        "Q": (0, 142, 255), "R": (108, 0, 255), "S": (237, 0, 255), "T": (255, 0, 38)
    }
    # 读取JSON文件
    with open(json_path, 'r') as f:
        data = json.load(f)
    # Load the image
    img = cv2.imread(mask_path)

    # 循环处理每个'title'
    for i, obj in enumerate(data["Label"]['objects']):
        title = obj['title']
        # 根据title分配颜色
        color = colors[title]
        # 读取多边形点坐标
        pts = np.vstack([np.asarray(poly[0], dtype=np.int32) for poly in obj['polygons']][:-1])
        # pts = np.array(obj['polygons'][-1])
        pts = pts.reshape((-1, 1, 2))
        # 创建空的mask图像
        mask = np.zeros_like(img[:, :, 0])
        # 填充多边形区域
        pts = cv2.convexHull(pts)
        cv2.fillConvexPoly(mask, pts, 1)

        # # 将mask转为彩色图像
        # mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
        # # 将mask与颜色融合
        # mask_rgb[:, :, 0] = np.where(mask == 1, color[0], mask_rgb[:, :, 0])
        # mask_rgb[:, :, 1] = np.where(mask == 1, color[1], mask_rgb[:, :, 1])
        # mask_rgb[:, :, 2] = np.where(mask == 1, color[2], mask_rgb[:, :, 2])

        # 将图像二值化
        thresh, binary = cv2.threshold(img[:,:,0], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        mask_intersect = cv2.bitwise_and(mask, binary)

        # 膨胀腐蚀
        kernel_eroded = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        eroded = cv2.erode(mask_intersect, kernel_eroded, iterations=1)
        binary = cv2.medianBlur(eroded, 15)

        if title.isalpha():  # 判断字符是否为字母
            title = ord(title.upper()) - ord('A') + 32  # 将字母转换为数字, 从33开始

        # 保存结果
        cv2.imwrite(os.path.join(save_path, str(int(data['External ID'].split('.')[0]) + 10000)+f'_{title}_0.jpg'), binary*255)

for json_name in tqdm(json_files):
    json_path = os.path.join(jsons_path, json_name)
    mask_path = os.path.join(masks_path, json_name.replace('.json','.jpg'))
    write_json_to_mask(json_path, mask_path, save_path)

# write_json_to_mask(r"E:\Datasets\xray\Segmentation\json_files\111.json",r'E:\Datasets\xray\Segmentation\teeth_mask\111.jpg', r'E:\Datasets\xray\testinstmask')