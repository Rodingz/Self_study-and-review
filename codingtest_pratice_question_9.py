# 문자열 밀기
A = "apple"
B = ""	
C = A
for i in range(len(A)):
    if A != B:
        C = C[len(C)-1] + C[0:len(C)-1]
        if C == B:
            answer = i+1
            break 
        else:
            answer = -1
    else:
        answer = 0

print(answer)


