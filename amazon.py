import string
letters = string.ascii_lowercase
d = dict()
count = 0

given = 'wwxyzwww'
final = ''
given+=' '
for i in letters:
    
    count+=1
    if count>=10:
        d[i] = str(count)+'#'
        continue
    d[i] = str(count) 
count =1
prev = 22
for i in given:
    
    if i == prev:
        count+=1
        print(i,end=' ')
        print(prev,end=' ')
        print(count)
        continue
    
    if count>1:
        final+='('+str(count)+')'
        count =1
        prev = i
        continue
    final+=d[i]
    prev = i
print(final)
