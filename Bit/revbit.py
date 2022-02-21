x = 3
temp = ''
top = 0
while x>0:
    if x&1 == 1:
        temp+= '1'
    else:
        temp+='0'
    top+=1
    x = x>>1
while len(temp)<32:
    temp+='0'
print(int(temp,2))