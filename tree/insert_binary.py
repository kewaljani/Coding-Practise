# Python program to insert element in binary tree
class newNode():
 
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None
         
def inorder(root):
    if not root:
        return 
    else :
        inorder(root.left)
        print(root.key)
        inorder(root.right)
""" Inorder traversal of a binary tree"""
def insert(temp,key):
    if not temp:
        return 
    if not temp.left and temp.right:
        temp.left =  newNode(key)
    if not temp.right and temp.left:
        temp.right = newNode(key)
    insert(temp.left,key)
    insert(temp.right,key)
# Driver code
if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(11)
    root.left.left = newNode(7)
    root.right = newNode(9)
    root.right.left = newNode(15)

    print("Inorder traversal before insertion:", end = " ")
    inorder(root)
 
    key = 12
    insert(root, key)
 
    print()
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)