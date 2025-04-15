import os

# 指定要重命名文件的文件夹路径
folder_path = r"E:\Datasets\xray\Json_morethan32"

# 获取文件夹中所有的文件名
file_names = os.listdir(folder_path)

# 遍历文件夹中的所有文件
for file_name in file_names:
    # 确认文件是图像文件（可根据需要修改）
    if file_name.endswith(".json") or file_name.endswith(".jpg"):
        # 构建新的文件名，将数字加上1000
        new_file_name = str(int(file_name.split(".")[0]) + 10000) + ".json"
        # 重命名文件
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
