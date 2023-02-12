cipher = "pfqallllabwaoclk"		
code = 2
answer = ""
for i in range(len(cipher)):
    if i % code == code-1:
        answer = answer + cipher[i]
print(answer)
