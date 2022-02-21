# dic = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
word ="apple"
k = 25
# def longestKInterspaceSubstring(word,k):
#     if len(word)<=1:
#         return word
#     res=""
#     substr=""
#     for i in range(0,len(word)-1):
#         substr=substr+word[i]
#         if len(substr)>len(res):
#                 res=substr
#         if >k:
#             if len(substr)>len(res):
#                 res=substr
#             substr=""
#     # print(substr)
#     return res
# print(longestKInterspaceSubstring(string,k))

max = 0
length = 1
sub = word[0]
maxstr = ""
for i in range(1,len(word)):
    # print("new = ",sub)
    if abs(ord(word[i])-ord(word[i-1]))>k:
        if len(sub)>len(maxstr):
            maxstr = sub
        sub = ""
        sub = word[i]
        continue
    sub +=word[i]
    # print(sub)
if len(sub)>len(maxstr):
    print(sub)
else:
    print(maxstr)
# print(maxstr)
#         # print(sub)
#         # break
# #     print("len = ",length , "str =",word[i])
# #     if val>k:
# #         print("breaked")
# #         if length> max:
# #             max = length
# #             sub+=string[i]
# #         # length = 1
# #         # continue
# #     sub+=string[i]
# # print(length)

    
