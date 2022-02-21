A = [4, 42,40, 26, 46]
B = 20
A.sort()
print(A)
# B = 20
low = 0
high = len(A)-1
collection = 0
while low<=high:
    mid = low+high//2
    # print(mid)
    for i in range(mid,len(A)):
        # print(i)
        collection = collection+abs(A[i]-A[mid])
    # print(collection)
    if collection == B:
        print("index found at",mid,"and collected = ",collection)
        break
    elif collection<B:
        high = mid-1
    elif collection>B:
        low=mid+1
    # print(low,mid,high)
    temp = collection
    collection = 0
# print(mid)
# print(temp,B) 


    