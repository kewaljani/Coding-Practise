class MinHeap:
    def __init__(self,maxValue):
        self.maxValue = maxValue
        self.lst = [None]*maxValue
        self.current = 0
    def parent(self,i): 
        return  int(i-1/2)
    def insert(self,val):
        print(x.lst)
        self.lst[self.current] = val
        i =  self.current
        while (i!=0 and self.lst[i]>self.lst[self.parent(i)]):
            temp = self.lst[i]
            self.lst[i]  =  self.lst[self.parent(i)]
            self.lst[self.parent(i)] = temp
            i = self.parent(i)
        self.current += 1
 
x = MinHeap(20)
x.insert(11)
x.insert(3)
x.insert(2)
x.insert(1)
x.insert(15)
x.insert(5)
x.insert(4)
x.insert(45)
print(x.lst)
