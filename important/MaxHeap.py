class MaxHeap:
    def __init__(self, max_size):
        self.data = [0]
        self.n = 0
        self.max_size = max_size
    
    def push(self, val):
        self.data.append(item)
        self.n+=1
        self.up(self.n)
       
    def pop(self):
        d = self.data[1]
        self.data[1] = self.data[self.n]
        self.data.pop()
        self.n -= 1
        self.down(1)
        return d
    
    def swap(self, i, j):
        t = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = t
    
    def down(self, fnode):
        index = fnode
        while index<=self.n//2:
            left = index*2
            right = index*2+1
            left_val = self.data[index] if left>self.n else self.data[left]
            right_val = self.data[index]if right>self.n else self.data[right]
            max_val = max(self.data[index], left_val, right_val)
            if self.data[index]==max_val:
                break
            elif left_val==max_val:
                self.swap(index, left)
                index = left
            else:
                self.swap(index, right)
                index= right
    def up(self, index):
        while index>1:
            f = index//2
            if self.data[f]<self.data[index]:
                self.swap(f, index)
                index = f
            else:return
    
    def build(self, data, size):
        self.n = size
        for d in data:
            self.data.append(d)
        for i in range(size//2, 0, -1):
            index = i
            self.down(index)
            
        self.n = size
        
    
    def sort(self, data):
        index = min(len(data), self.max_size)
        self.build(data, index)
        res = []
        while self.n>0:
            res.append(self.data[1])
            self.n = self.n-1
            if self.n>0:
                self.data[1]=self.data[self.n+1]
                self.down(1)
        return res
        

so = MaxHeap(20)
print(so.sort([3,5,7,1,2,4,6,8,12,6,1,2,0,9,90,34,6]))
        