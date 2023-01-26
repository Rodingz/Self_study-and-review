my_str = "abcdef123"		
n = 3
answer = []
if len(my_str) % n ==0:
    a = len(my_str)/n
else:
    a = int(len(my_str)/n) +1
for i in range(int(a)):
    if i != int(len(my_str)/n)+1:
        answer.append(my_str[n*i:n*(i+1)])
    else:
        answer.append(my_str[n*i:])
print(answer)

