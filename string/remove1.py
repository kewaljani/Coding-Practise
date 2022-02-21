A = "phmjjmap"
n = len(A)

# Counting number of
# characters that
# should be changed.
count = 0
for i in range(0, int(n / 2)) :
    if (A[i] != A[n - i - 1]) :
        count = count + 1

# If count of changes
# is less than
# or equal to 1
# print(count)
if(count <= 1) :
    print(count)
else :
    print(count)