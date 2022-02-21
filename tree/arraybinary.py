tree = [None]*10

def root(key):
    if tree[0] != None:
        print("alreay root node set")
        return
    else:
        tree[0] = key


def left_child(key,parent):
    if tree[parent]== None:
        print("no parent fount")
    else:
        tree[(parent*2)+1] = key


def right_child(key,parent):
    if tree[parent]== None:
        print("no parent fount")
    else:
        tree[(parent*2)+2] = key


def print_tree():
    for i in range(10):
        if tree[i] != None:
            print(tree[i], end="")
        else:
            print("-", end="")
    print()

root('A')
right_child('C', 0)
left_child('D', 1)
right_child('E', 1)
right_child('F', 2)
print_tree()