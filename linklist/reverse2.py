def lPalin(self, A):
    prev = A
    rev = ListNode(None)
    tail = None
    while A:
        temp  = ListNode(A.val)
        if not tail:
            tail = temp
        else:
            temp.next = tail
            tail = temp
        rev.next = tail
return rev


print(lPalin(A))