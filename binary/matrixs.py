A = [
  [1, 1, 2, 2, 5, 6, 6, 6, 7],
  [9, 10, 10, 12, 12, 13, 14, 21, 21],
  [23, 26, 26, 29, 29, 31, 32, 35, 37],
  [38, 39, 39, 39, 41, 41, 42, 42, 43],
  [45, 45, 46, 46, 46, 47, 48, 48, 51],
  [51, 51, 54, 54, 54, 54, 56, 58, 59],
  [60, 61, 61, 62, 63, 64, 65, 66, 67],
  [67, 67, 70, 70, 71, 73, 73, 73, 74],
  [74, 79, 79, 80, 82, 84, 84, 84, 87],
  [89, 93, 94, 94, 97, 98, 98, 98, 98]
]
B = 64
flag = 0


for i in range(len(A)):
    # print(A[i][0],B)
    if A[i][len(A[i])-1]>=B and A[i][0]<=B:
        print("Index = ",i)
        flag = 1
        # print(flag)
        if A[i][len(A[i])-1] == B or A[i][0]==B:
            print(1)
        else:
            front = 0
            last = len(A[0])-1
            # 
            while front<=last:
                print(front,last)
                
                mid = front + (last-front)//2
                print("Mid = ",A[i][mid])
                if A[i][mid]==B:
                    print(1)
                    break
                elif A[i][mid]>B:
                    last = mid-1
                elif A[i][mid]<B:
                    front = mid+1
                # break
            print(0)
    if flag==1:
        break
else:
    print(0)