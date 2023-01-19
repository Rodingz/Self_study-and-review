array = [9, 10, 11, 8]	
answer = []
answer = [0]
counter = 0
while counter < len(array):
    if array[counter] > answer[0]:
        answer.clear()
        answer.append(array[counter])
        answer.append(counter)
    counter += 1
print(answer)

