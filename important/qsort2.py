'''
对有很多重复值的数组进行优化(也适用一般快排)
'''
class Solution:
    def qs(self, data, start, end):
        if start>=end:return
        p1, p2 = start, end
        p = start
        tag = data[start]
        while p<=p2:
            if data[p]==tag:
                p+=1
            elif data[p]>tag:
                self.swap(data, p, p2)
                p2-=1
            else:
                self.swap(data, p, p1)
                p1+=1
                p+=1
        self.qs(data, start, p1-1)
        self.qs(data, p2+1, end)
        
    def swap(self, data, i, j):
        t = data[i]
        data[i]=data[j]
        data[j]=t
                
   
import random
data = [random.randint(0, 10000) for _ in range(100)]
so = Solution()
so.qs(data, 0, len(data)-1)
pre = data[0]
for d in data[1:]:
    if d<pre:
        print('error')
        break
    else:
        pre = d
print(data[:100])