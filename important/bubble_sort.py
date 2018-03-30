# bubble sort with early stopping
class Solution:
    def bs(self, data):
        if len(data)<=1:return
        n = len(data)
        for i in range(n-1):
            count = 0
            for j in range(n-1, i, -1):
                if data[j]<data[j-1]:
                    self.swap(data, j-1, j)
                    count += 1
            if count==0:
                break
        
    def swap(self, data, i, j):
        t = data[i]
        data[i] = data[j]
        data[j] = t


import random
#data = [random.randint(0, 100) for _ in range(10000)]
data = list(range(10000))
so = Solution()
so.bs(data)
pre = data[0]
for d in data[1:]:
    if d<pre:
        print('error')
        break
    else:
        pre = d
print(data[:100])