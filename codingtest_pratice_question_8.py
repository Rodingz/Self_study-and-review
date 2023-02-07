num = 29183
k = 1
answer = 0
num = str(num)
for i in range(len(num)):
    if int(num[i]) == k:
        answer = i+1
        break
    else:
        answer = -1
print(answer)

#i = 0, 2 asnwer = -1
#i = 1, 9 answer = -1
#i = 2, 1 answer = 3
