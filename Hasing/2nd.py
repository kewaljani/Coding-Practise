sumeve = 0
sumodd = 0
numbers = [-7,0,8,-5,-10]
if len(numbers)%2 !=0:
    for i in range(len(numbers)//2):
        sumeve += numbers[2*i]
        sumodd +=numbers[2*i+1]
        # print(2*i)
    sumeve+=numbers[2*(i+1)]
else:
    for i in range(len(numbers)//2):
        sumeve += numbers[2*i]
        sumodd +=numbers[2*i+1]
        # print(2*i)
print(sumeve,sumodd)
if sumeve>sumodd:
    print("even")
elif sumeve<sumodd:
    print("odd")
else:
    print("equal")
