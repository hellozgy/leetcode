class Stack:
    def __init__(self):
        self.data = []
    def push(self, v):
        self.data.append(v)
    def pop(self):
        return self.data.pop()
    def empty(self):
        return len(self.data)==0

class queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.tag = 'push'
    
    def push(self, v):
        if self.tag=='push':
            self.stack1.push(v)
        else:
            self.tag='push'
            while not self.stack2.empty():
                self.stack1.push(self.stack2.pop())
            self.stack1.push(v)
    
    def pop(self, v)
        if self.tag=='pop':
            self.stack2.pop()
        else:
            self.tag='pop'£º
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()
        
    def empty(self):
        return self.stack1.empty() and self.stack2.empty()
       