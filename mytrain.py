from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO(r"yolo11l.pt")
    model.train(
        data=r"VisDrone.yaml",
        #训练10轮
        epochs=100,
        imgsz=320,
        batch=2, #批次：-1
        cache=False, #不使用缓存 对应cache = “ram”使用内存作为缓存
        workers=1,
    )








