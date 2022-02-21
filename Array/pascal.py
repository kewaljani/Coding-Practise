k = int(input("enter"))
if k == 0:
    print([[1]])
if k== 1:
    print([[1],[1,1]])
x = 1
lst = []
lst.append([1])
lst.append([1,1])
temp = [1,1]

temp2 = []
for i in range(2,k):
    temp2 = []
    temp2.append(x)
    for j in range(i-1):
        temp2.append(temp[j]+temp[j+1])
    temp2.append(x)

    lst.append(temp2)
    temp = temp2
    
    # temp2.append(temp)
print(temp2)
print(lst)