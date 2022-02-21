string = ['code' ,'doce', 'coed', 'framer']

# string = sorted(string,key=len)
# string.remove('doce')
# print("".join(sorted(string[0])))
dic = dict()
lst = []
for i in range(len(string)):
    if "".join(sorted(string[i])) in dic:
        # print(string[i])
        # string.remove(string[i])
        continue
    else:
        dic["".join(sorted(string[i]))] = 1
        lst.append(string[i])
# print(lst)
print(sorted(lst,key = "len"))