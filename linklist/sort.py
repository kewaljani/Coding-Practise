# dic = {0:0,1:0}
# while A!=None:
#     dic[A.val]+=1
#     A = A.next
# # print(dic)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
dic = {0:1,1:1}
temp = ListNode
while dic[0]!=0:
    temp.val=0
    temp.next = ListNode
    temp = temp.next
    dic[0]-=1
    print(dic)

while dic[1]!=0:
    temp.val = 1
    temp.next = ListNode
    temp = temp.next
    dic[1]-=1
    print(dic)
while temp!=None:
    print(temp.val)
    temp  = temp.next