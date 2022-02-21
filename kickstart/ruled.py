def Solve(x,dic):
    for i in range(x):
        city = input()
        if city[-1] in  dic:
            print(city,"is ruled by Alice.")
        elif city[-1] == 'y':
            print(city,"is ruled by nobody.")
        else:
            print(city,"is ruled by Bob.")

x =  int(input())
dic = {'a':1,'e':1,'i':1,'o':1,'u':1}
Solve(x,dic)