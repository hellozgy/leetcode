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
            val = self.data[index]
            left_val = self.data[left]
            right_val = self.data[right] if right <= self.n else val
            if min(val, left_val, right_val) == val:
                return
            elif min(val, left_val, right_val) == left_val:
                self.swap(index, left)
                index = left
            else:
                self.swap(index, right)
                index = right
                
    
    def build(self, data):
        for d in data:
            self.data.append(d)
            self.n += 1
        for index in range(self.n//2, 0, -1):
            self.down(index)
    
    def pop(self):
        d = self.data[1]
        self.data[1] = self.data[self.n]
        self.n -= 1
        self.down(1)
        return d
        
      
    def sort(self, data):
        self.build(data)
        res = []
        while self.n > 0:
            res.append(self.pop())
        
        return res
        

so = MinHeap()
data = [1,2,3,89,12,45,1,2,7,90,23,5,6,78,123,451,236]
res = so.sort(data)
print(res)