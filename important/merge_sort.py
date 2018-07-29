class MinHeap:
    def __init__(self, max_size=100):
        self.data = [0]
        self.n = 0
        self.max_size = max_size
    
    def swap(self, i, j):
        tmp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = tmp
    
    
    def down(self, index):
        while index<=self.n//2:
            left , right = index * 2, index * 2 + 1
            val = self.data[index][0]
            left_val = self.data[left][0]
            right_val = self.data[right][0] if right <= self.n else val
            if min(val, left_val, right_val) == val:
                return
            elif min(val, left_val, right_val) == left_val:
                self.swap(index, left)
                index = left
            else:
                self.swap(index, right)
                index = right
    def up(self, index):
        while index>1:
            father = index//2
            if self.data[father][0]>self.data[index][0]:
                self.swap(father, index)
                index = father
            else:
                return
            
    
    def build(self, data):
        for d in data:
            self.data.append(d)
            self.n += 1
        for index in range(self.n//2, 0, -1):
            self.down(index)
    
    def push(self, item):
        self.n += 1
        self.data.append(item)
        self.up(self.n)
    
    def pop(self):
        d = self.data[1]
        self.data[1] = self.data[self.n]
        self.data.pop()
        self.n -= 1
        self.down(1)
        return d
        
      
    def sort(self, data):
        self.build(data)
        res = []
        while self.n > 0:
            res.append(self.pop())
        
        return res
    
    def empty(self):
        return self.n==0

class Solution:
    def msort(self, datas):
        heap = MinHeap()
        for i in range(len(datas)):
            if datas[i]:
                heap.push([datas[i][0], i, 1])
        res = []
        while not heap.empty():
            v, list_index, item_index = heap.pop()
            res.append(v)
            if item_index<len(datas[list_index]):
                heap.push([datas[list_index][item_index], list_index, item_index+1])
        return res
        
        
        
datas=[
[1,4,7,9,9,10,51],
[6,51,111,454,2111,111111,5333333],
[5,10,20,40,80,90]]
so = Solution()
print(so.msort(datas))