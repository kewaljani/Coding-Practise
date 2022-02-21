arr = [1,2,2,3,1]
# arr = [1,2,1,3,2]
degree = 0
dic = dict()
location = dict()
location2 = dict()
for i in range(len(arr)):
    if arr[i] in dic:
        dic[arr[i]]+=1
        if dic[arr[i]]>degree:
            degree = dic[arr[i]]
    else:
        dic[arr[i]] = 1
        location[arr[i]] = i
    location2[arr[i]] = i
# for i in range()
# print(dic)
print(degree)
# min = 100000
print(location)
print(location2)
for key,values in dic.items():
    print(location2[key] - location[key]+1)
#     if values == degree:
#         # print(degree)
#         if min>location2[key] - location[key]+1:
#             min = location2[key] - location[key]+1
# print(min)


