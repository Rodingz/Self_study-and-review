answer = 0

t='3141592'
p='271'
part = []
counter = 0
while counter <= (len(t) - len(p)):
    part.append(t[counter:counter + len(p)])
    counter =+ 1
print(part)
for i in part: 
    if i > int(p):
        #answer +=1
print(answer)