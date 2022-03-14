A = [ "cat", "dog", "god", "tca" ]
dic= dict()
for i in range(len(A)):

    if "".join(sorted(A[i])) in dic:
        dic["".join(sorted(A[i]))].append(i+1)
    else:
        dic["".join(sorted(A[i]))] = [i+1]
final = []
for key,val in dic.items():
    final.append(val)
print(final)