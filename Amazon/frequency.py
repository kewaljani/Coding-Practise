S = "abbbcacbcdce"
maximum = 0
dic = dict()
for i in range(len(S)):
    if S[i] in dic:
        dic[S[i]][0]+=1
        dic[S[i]][1].append(i)
    else:
        dic[S[i]] = [1,[i]]
    # print(type(dic['a'][1]))

print(dic)
# for i in range(len(dic)):
#     for j in range(i+1,len(dic)):

# for i in S:
#     if i in dic:
#         dic[i][0]+=1
#         # print(dic[i][0])
#         if dic[i][0]>maximum:
#             maximum = dic[i][0]
#     else:
#         dic[i] = [1,set(i)]
# print(len(dic['b'][1]))
acount = 0
bcount = 0
for i in range(len(dic['a'][1])+len(dic['b'][1])):
    f1 ,f2, l1 ,l2 = 0,0,len(dic['a'][1]),len(dic['b'][1])
    # if f1<=f2 and l1<=l2 and l1>=f2:
    #     substring_len = f2-l1
        
    elif 



        
        # print(f1,f2,l1,l2)
print(dic,maximum)
