import numpy
import cv2

a = [1,2,3,4,5]
b = numpy.array([1,2,3,4,5])

# array --> 한가지 data type
# list --> 여러가지 data type 
print(a[2]) # 3 --> integer
print(a[2:4]) # [3,4] --> list (마지막 전것까지)

c = numpy.array([[0,4,5,5,6],[4,5,6,3,6],[4,6,7,9,4]]) # nd --> [] 개수
print(c[0])
print(c[0][0])
print(c[1:, 1])
print(c[1:][1])
print(2*c) # 이런건 array만 가능 
print(2*a) # list 는 [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

print(len(c))
print(len(c[0]))
print(c.ndim)
print(c.shape) # 같은 shape 만 연산 가능 

