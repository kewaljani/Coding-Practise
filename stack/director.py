A = "/../"
A = A.split("/")
stack = []
for i in A:
    print(i.isalpha())
    if i.isalpha():
        stack.append(i)
    elif i  == '.':
        pass
    elif i =='..' and stack:
        stack.pop()
    else:
        pass
if stack:
    print("/"+stack[-1])
else:
    print("/")
# returnpython("/"+stack[-1])