import os
import random
import shutil

# 定义文件夹路径
source_folder = r'E:\yoloStady\ultralytics-8.3.163\make_dataset\images'
train_folder = r'E:\yoloStady\ultralytics-8.3.163\make_dataset\xz_dataset\images\train'
val_folder = r'E:\yoloStady\ultralytics-8.3.163\make_dataset\xz_dataset\images\val'

# 获取文件夹中的所有图片文件
all_images = [f for f in os.listdir(source_folder) if f.endswith('.jpg')]

# 随机选择20%的图片
sample_size = int(len(all_images) * 0.2)
random_images = random.sample(all_images, sample_size)

# 按照70%和30%的比例划分训练集和验证集
train_images = random_images[:int(sample_size * 0.7)]
val_images = random_images[int(sample_size * 0.7):]

# 移动图片到相应的文件夹
def move_images(image_list, target_folder):
    for image in image_list:
        source_path = os.path.join(source_folder, image)
        target_path = os.path.join(target_folder, image)
        shutil.move(source_path, target_path)
        print(f"Moved {image} to {target_folder}")

# 移动到训练集和验证集文件夹
move_images(train_images, train_folder)
move_images(val_images, val_folder)

print("图片移动完成。")
