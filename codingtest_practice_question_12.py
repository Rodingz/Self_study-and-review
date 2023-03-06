s = "123"	
a = ""
answer = ""
for i in s:
    a = a + i
    if a == "one" or a =="1":
        answer = "1"+ answer
        a = ""
    if a == "two" or a =="2":
        answer = "2"+ answer
        a = ""
    if a == "three" or a =="3":
        answer = "3"+answer
        a = ""
    if a == "four" or a =="4":
        answer = "4"+ answer
        a = ""
    if a == "five" or a =="5":
        answer = "5"+ answer
        a = ""
    if a == "six" or a == "6":
        answer = "6"+ answer
        a = ""
    if a == "seven" or a == "7":
        answer = "7"+ answer
        a = ""
    if a == "eight" or a =="8":
        answer = "8"+ answer
        a = ""
    if a == "nine" or a =="9":
        answer = "9"+ answer
        a = ""
print(int(answer[::-1]))


