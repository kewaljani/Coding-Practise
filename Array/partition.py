A = 5
B = [1, 2, 3, 0, 3]
total = sum(B)
if total % 3 == 0:
    target = total // 3
else:
   print("flase") 
print("target = ",target)
ans = 0
f = 0
s = 0
for i in range(A - 1):
    s += B[i]
    if s == 2 * target:
        ans += f
    if s == target:
        f += 1
print(ans)