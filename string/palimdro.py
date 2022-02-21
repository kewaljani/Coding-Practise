A= "1a2"
temp = ""
temp = ""
for i in A:
    if i.isalnum():
        temp+=i
# print(temp)
# print(temp[0:len(temp)//2])
# print(temp[len(temp):(len(temp)//2)-1:-1])
if len(temp)%2==0:
    if temp[0:len(temp)//2].upper() == temp[len(temp):(len(temp)//2)-1:-1].upper():
        print(1)
    else: 
        print(0)
else:
    if temp[0:len(temp)//2].upper() == temp[len(temp):(len(temp)//2):-1].upper():
        print(1)
    else:
        print(0)