import ipdb

class Stack:

    def __init__(self, items=[], limit = 10):
        self.items = items
        self.length = len(self.items)
        self.limit = limit
    
    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def push(self, value):
        if self.length < self.limit:
            self.items.append(value)
            self.length += 1
       
    def pop(self):
        if self.length != 0:
            self.length -= 1
            return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return self.length

    def full(self):
        if self.length == self.limit:
            return True
        else:
            return False
        
    def search(self, target):
            if self.length > 1:
                print(self.items.index(target) - len(self.items))
                return self.items.index(target) - len(self.items) 
            else:
                return 0
    
stack = Stack([5, 6, 7, 8])
print(stack.items.index(5))
stack.push(0)
stack.isEmpty()
stack.search(5)
print(stack.search(5))
print(stack.items)
#print(stack.items)
#print(stack.length)
#print(stack.isEmpty())
#print(stack.search(5))

