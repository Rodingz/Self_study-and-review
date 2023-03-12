phone_number = "027778888"		
answer = ''
counter = 0
for i in phone_number[::-1]:
    if counter < 4:
        answer = answer + i
        counter +=1
    else:
        answer = answer + "*"
answer = answer[::-1]
print(answer)

    
    
