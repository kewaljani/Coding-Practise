
def ispal( s):
    return s == s[::-1]
    
def solve2(A):
    match = 0
    for idx in reversed(range(1, len(A) + 1)):
        if ispal(A[:idx]):
            match = idx
            break
    return len(A) - match
def gen_lsp(p):
    lsp = [0 for i in range(len(p))]
    print(lsp)
    j = 0
    for i in range(1, len(lsp)):
        print(lsp,i,j)
        while j != 0 and p[i] != p[j]:
            j = lsp[j - 1]
            print("enter")
            print(j)
        if p[i] == p[j]:
            lsp[i] = j + 1
            j = j + 1
        else:
            lsp[i] = 0
        # print(lsp,j)
    return lsp
A = "AAA"
def solve(A):
    s = A + '_' + A[::-1]
    print(s)
    lsp = gen_lsp(s)
    return len(A) - lsp[-1]
print(solve(A))