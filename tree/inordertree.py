# Non recursive method



class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None



def inorder(root):
    if not root:
        return 
    else:
        s = []
        s.append(root)
        while(s):
            temp = s.pop(0)
            while(temp!=None):
                s.append(temp.left)
                temp = temp.left
            current = s.pop(0)
            print(current)
            # print(temp.val)
            # temp = temp.right


x = Node(10)
x.right = Node(20)
x.left = Node(5)

inorder(x)