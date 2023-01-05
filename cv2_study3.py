import cv2 
  
img = cv2.imread("C:/Users/kevin/Desktop/python_selfst/img_f1.jpg") 
  
# make sure that you have saved it in the same folder
# You can change the kernel size as you want
blurImg = cv2.blur(img,(5,100)) 
cv2.imshow('blurred image',blurImg)
  
cv2.waitKey(0)
cv2.destroyAllWindows()