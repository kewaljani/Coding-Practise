intervals = [1,3],[2,6],[8,10]
start = intervals[1][0]
end = intervals[0][1]
temp = []
final = []
flag = 0
for i in range(len(intervals)-1):
    end = intervals[i][1]
    start = intervals[i+1][0]
    if start < end:
        tempintervals[i][0],0
    final.append(temp)
print(final)        

