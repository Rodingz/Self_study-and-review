import cv2
print(cv2._version_)
img1 = cv2.imread('"C:\Users\kevin\Desktop\python_selfst\img_f1.jpg"') # 이미지 불러오기
img1 = cv2.imread('"C:\Users\kevin\Desktop\python_selfst\img_f1.jpg"', 1)

print(type(img1))
cv2.imshow('image1', img1) # 이미지 출력을 위한 위도우 창 호출
cv2.waitkey(0) # 사용자의 입력을 기다림
cv2.destroyAllWindows # 실행중인 프로그램 종료

