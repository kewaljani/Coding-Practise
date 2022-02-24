
lst = []
while A!=None:
    lst.append(A.val)
    A =A.next
# print(lst)
newnode = ListNode
newnode(lst[-1])
lst.pop()
while len(lst) != 1:
    temp = lst.pop()
    newnode.val = temp
    newnode.next = ListNode
    newnode.next  = newnode
return newnode