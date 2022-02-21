x = int(input())
lst = []
rout = dict()
for i in range(x):
    x = input().split(" ")
    lst.append([])
    lst[i].append(int(x[0]))
    lst[i].append(int(x[1]))
low = lst[0][0]
high = lst[0][1]
count = 0
print(lst)
for i in range(1,len(lst)):
    print(low)
    print(high)
    if lst[i][0]>=low and lst[i][0]<=high:
        count+=1
        continue
    else:
        low = lst[i][0]
        high = lst[i][1]
        count+=1
print(count)
