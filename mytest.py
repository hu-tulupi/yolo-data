from ultralytics import YOLO

model = YOLO(r"yolov8m.pt")
#获取模型任务类型
print(model.task)
#获取模型可以识别的类型
print(model.names)
#打印出所有参数的数量
print(sum(p.numel() for p in model.parameters()))