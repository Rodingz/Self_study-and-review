import cv2
print(cv2.__version__)
img1 = cv2.imread("C:/Users/kevin/Desktop/python_selfst/img_f1.jpg") # 이미지 불러오기
print(img1.ndim)
print(img1.shape)