class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min==None:self.min = x
        else:self.min = min(x, self.min)
        self.data.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        d = self.data.pop()
        if d==self.min:
            self.min = min(self.data) if self.data else None
        return d
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()