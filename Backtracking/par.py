a= 6
temp = ['(',')']
final = []
ans = []
count = 0
def pargen(a,i,temp,final,final2,count):
    # print(final,temp[i])
    # print(final)
    # if final : 
    #     print("inside")
    #     print(final,temp[i])
    #     if final[-2] == "(" and temp[-1] == ")":
    #                 # print("inside")
    #                 # final2.append(final)
    #                 final.pop()
                    # continue
    
    if count == a :
        if ispara(list(final)):
            ans.append("".join(list(final)))
        return
    for i in range(2):
        # 
        # if final:
        #     print(final)
        #     if final[-1] == "(" and temp[i] == ")":
        #         print(final[-1])
        #         final.pop()
        #         continue
        # print(final,temp[i])
        final.append(temp[i])
        pargen(a,i,temp,final,final2,count+1)
        final.pop()
def ispara(lst):
    stack = []
    print("inside:",lst)
    if lst[0] == ")":
        return False
    for i in lst:
        # print(stack)
        if stack:
            if stack[-1] == "(" and i == ")":
                # print(stack,i)
                stack.pop()
                continue
        stack.append(i)
        # print(stack)
    if len(stack) == 0:
        return True
    else:
        return False
    # print("outside : ",len(stack))
    

pargen(a,0,temp,final,ans,0)
print(ans)
