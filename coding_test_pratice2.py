n = 930211
n = str(n)
l = len(n)
counter = 0
answer = 0
while counter < l:
    answer = answer + int(n[counter])
    counter += 1
print(answer)
