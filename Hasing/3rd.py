# Python3 program to count the number of substrings
# divisible by 4.
 
def countDivisbleby4(s):
    n = len(s)
     
    # In the first loop we will count number of
    # 0's, 4's and 8's present in the string
    count = 0
    for i in range(0,n,1):
        if (s[i] == '3' or s[i] == '6' or s[i] == '9' ):
            count += 1
    for i in range(0,n - 1,1):
        h = (ord(s[i]) - ord('0')) * 10 + (ord(s[i+1]) - ord('0'))
        if (h % 3 == 0):
            count = count + i + 1
     
    return count
 
# Driver code to test above function
if __name__ == '__main__':
    s = "303"
    print(countDivisbleby4(s))