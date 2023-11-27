import torch
import numpy as np
import yaml

class ImageDetect:
    model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5s', force_reload=True)
    data = {}
    
    # 클래스 생성 시 자동으로 호출되는 생성자 함수
    def __init__(self):
        with open('coco.yaml', 'r', encoding='UTF-8') as f:
            self.data = yaml.full_load(f)['names']
    # self : 
    def detect_img(self, img):
        result = self.model(img).xyxyn[0].numpy()
        return result