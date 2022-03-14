def lszero( arr):
    hash_map = {}
    index = [0,0]
    # Initialize result
    max_len = 0

    # Initialize sum of elements
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]

        if arr[i] is 0 and max_len is 0:
            max_len = 1

        if curr_sum is 0:
            max_len = i + 1
            index = [0,i]
        if curr_sum in hash_map:
            if  max_len<i-hash_map[curr_sum]:
                max_len = i-hash_map[curr_sum]
                index  = [hash_map[curr_sum],i]
                
                
            
        else:

            hash_map[curr_sum] = i
    return index

A = [ 1, 2, -3, 3 ]
print(lszero(A))