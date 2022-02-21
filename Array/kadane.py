lst = [-2, -3, 4, -1, -2, 1, 5, -3]

maxe = 0
maxf = 0
for i in range(len(lst)):
    maxe += lst[i]
    if maxf<maxe:
        maxf = maxe
    if maxe < 0 :
        maxe = 0
print(maxf)