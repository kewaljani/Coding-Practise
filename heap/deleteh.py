class MinHeap:
    def __init__(self,capacity):
        self.lst = [None]*capacity    
        self.current = 0
        self.capacity = capacity
        self.temperory = None
    def parent(self,i): 
        return  int(i-1/2)
    def insert(self,val):
        self.lst[self.current] = val
        i =  self.current
        while (i!=0 and self.lst[i]<self.lst[self.parent(i)]):
            temp = self.lst[i]
            self.lst[i]  =  self.lst[self.parent(i)]
            self.lst[self.parent(i)] = temp
            i = self.parent(i)
        self.current += 1    
    def rearrange(self, i):
        self.temperory =  self.lst[i]
        val = -100
        self.lst[i] = val
        while (i!=0 and self.lst[i]<self.lst[self.parent(i)]):
            temp = self.lst[i]
            self.lst[i]  =  self.lst[self.parent(i)]
            self.lst[self.parent(i)] = temp
            i = self.parent(i)
    def left(self,i):
        return (2*i+1)
    def right(self,i):
        return(2*i+2)
    def removeMin(self):
        root = self.lst[0]
        self.lst[0] = self.lst[self.current-1]
        self.lst[self.current-1] = None
        self.current-=1
        x = self.heapify(0)
        

    def deleteh(self,index):
        self.rearrange(index)
        self.removeMin()
        print(self.temperory)
        return self.temperory
        
    def heapify(self,i):
        smallest = i
        left = 2*i+1
        right = 2*i+2
        if (left<self.current and self.lst[self.left(i)]<self.lst[i]):
            smallest = self.left(i)
        if (right<self.current and self.lst[self.right(i)]<self.lst[smallest]):
            smallest = self.right(i)
        if (smallest != i):
            temp = self.lst[i]
            self.lst[i] = self.lst[smallest]
            self.lst[smallest] = temp
            self.heapify(smallest)

            

x = MinHeap(20)
x.insert(20)
x.insert(40)

print(x.lst)
x.insert(30)
x.insert(50)
x.insert(90)
x.insert(35)
newlst = []
for i in range(x.current):
    newlst.append(x.deleteh(0))


print(newlst)
