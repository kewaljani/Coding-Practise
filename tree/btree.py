class newNode:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

def inorder(root):
    if not root:
        return 
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def insert(root,key):
    if not root:
        root = newNode(key)
        return
    q = []
    q.append(root)
    while(len(q)):
        temp = q[0]
        q.pop(0)
        if not temp.left:
            temp.left= newNode(key)
            break
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right = newNode(key)
            break
        else:
            q.append(temp.right)
def delete_deapest(root, d_node):
    q=[]
    q.append(root)
    while(len(q)):
        temp = q[0]
        q.pop(0)
        if temp == d_node:
            temp = None
            return
        if temp.right:
            if temp.right == d_node:
                temp.right = None
                break
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left == d_node:
                temp.left = None
                break
            else:
                q.append(temp.left)



def delete(root, key):
    if not root:
        return None
    if not root.left and  not root.right:
        if root.data == key:
            return None
        else:
            return root
    key_node = None
    q= []
    q.append(root)
    while(len(q)):
        temp = q[0]
        q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.data 
        delete_deapest(root, temp)
        key_node.data = x
    return root
     




if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(8)
    root.left.left = newNode(7)
    insert(root,12)
    insert(root,9)
    print("Before Deletion :")
    inorder(root)
    root = delete(root,8)
    print("After Deletion :")
    inorder(root)
