import cv2
import numpy as np

def resize_images(image1, image2):
    """调整两张图片为相同大小"""
    h1, w1 = image1.shape[:2]
    h2, w2 = image2.shape[:2]
    h, w = min(h1, h2), min(w1, w2)
    return cv2.resize(image1, (w, h)), cv2.resize(image2, (w, h))

def blend_faces(image1, image2, alpha=0.5):
    """融合两张图片"""
    image1, image2 = resize_images(image1, image2)
    blended = cv2.addWeighted(image1, alpha, image2, 1 - alpha, 0)
    return blended
