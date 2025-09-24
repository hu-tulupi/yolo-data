
from ultralytics import YOLO

model = YOLO(r"E:\yoloStady\ultralytics-8.3.163\ultralytics-8.3.163\runs\detect\train2\weights\best.pt")  #用yolo11n.pt这个模型预测（选择yolo模型）
model.predict(
    source=r"E:\yoloStady\videoTest\video3\images(1)\images\9月23日.mp4",
    # source=r"E:\yoloStady\imagesTest",
    #source=r"ultralytics\assets", 预测ultralytics\assets中所有的照片（可以复制地址替换图片或者视频）
    # 对预测一些额外的要求
    # save = Ture -》保存一下预测结果，对应save = False
    # show = False -》不用立刻显示结果，对应show = True
    save= True,
    show= False,
    # line_width=8,调整线的粗细
    # visualize = True,显示参数

)