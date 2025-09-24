import cv2
import os
from tqdm import tqdm

# 设置视频文件夹路径和保存图片的文件夹路径
video_folder = r"E:\yoloStady\ultralytics-8.3.163\make_dataset\videos"  # 视频文件夹路径
image_folder = r"E:\yoloStady\ultralytics-8.3.163\make_dataset\images"  # 图片保存文件夹路径

# 如果保存图片的文件夹不存在，就创建它
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# 设置每秒提取的帧数，可以根据需求进行调整
frames_per_second = 10  # 例如：每秒提取5帧

# 获取视频文件夹下所有的 .mp4 文件
video_files = [f for f in os.listdir(video_folder) if f.endswith('.MP4')]

# 遍历每个视频文件
for video_file in video_files:
    # 拼接出视频文件的完整路径
    video_path = os.path.join(video_folder, video_file)

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"无法打开视频文件: {video_file}")
        continue

    # 获取视频的一些信息
    fps = cap.get(cv2.CAP_PROP_FPS)  # 视频的帧率（每秒多少帧）
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 视频的总帧数
    video_name = os.path.splitext(video_file)[0]  # 获取视频文件名，不带扩展名

    # 计算每隔多少帧提取一次图片（根据帧率和每秒提取的帧数）
    frame_interval = int(fps // frames_per_second)

    # 使用进度条来显示当前处理进度
    pbar = tqdm(total=total_frames, desc=f"处理视频: {video_name}", unit="帧")

    # 图片序号，从1开始
    image_counter = 1

    # 从视频读取每一帧
    while True:
        ret, frame = cap.read()  # 读取一帧
        if not ret:
            break  # 如果没有读取到帧，说明视频播放完了，退出循环

        # 判断是否需要提取当前帧
        current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))  # 获取当前帧的编号
        if current_frame % frame_interval == 0:
            # 生成图片的文件名，格式为：视频名_图片序号.jpg
            image_filename = f"{video_name}_{image_counter:05d}.jpg"
            image_path = os.path.join(image_folder, image_filename)

            # 保存当前帧为图片
            cv2.imwrite(image_path, frame)

            # 图片序号加1
            image_counter += 1

        pbar.update(1)  # 更新进度条，表示已经处理了一帧

    # 处理完视频，释放资源
    cap.release()
    pbar.close()  # 关闭进度条

print("所有视频处理完成！")
