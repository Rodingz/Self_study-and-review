#분수의 덧셈
numer1 = 1
denom1 = 12
numer2 = 3
denom2 = 8
list = []
for i in range(1,denom1):
    if denom1 % i ==0 and denom2 % i ==0:
        list.append(i)
print(max(list))


    


