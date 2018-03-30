class Solution:
    def qs(self, data, start, end):
        if start>=end:return
        p1, p2 = start+1, end
        tag = data[start]
        while p1<p2:
            while p1<p2 and p1<end and data[p1]<=tag:
                p1+=1
            while p2>p1 and p2>start and data[p2]>=tag:
                p2-=1
            if p1<p2:
                self.swap(data, p1, p2)
                p1+=1
                p2-=1
        if data[p1]<=tag:
            self.swap(data, start, p1)
            self.qs(data, start, p1-1)
            self.qs(data, p1+1, end)
        else:
            self.swap(data, start, p1-1)
            self.qs(data, start, p1-2)
            self.qs(data, p1, end)

        
    def swap(self, data, i, j):
        t = data[i]
        data[i]=data[j]
        data[j]=t
                
import random
data = [random.randint(0, 100) for _ in range(1000)]
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