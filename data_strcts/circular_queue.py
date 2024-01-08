

class CQUeue:
    def __init__(self, maxValu):
        self.maxValu = maxValu
        self.items = maxValu * [None]
        self.start = -1
        self.end = -1 
    
    def __str__(self):
        res = [str(i) for i in self.items]
        return " ".join(res) 
    
    def isEmpty(self):
        
        if self.start == -1 and self.end == -1:
            return True 
        return False 
    
    def isFull(self):
        if self.start == 0 and self.end == self.maxValu-1:
            return True 
        elif self.end == self.start -1:
            return True 
        return False 
    
    def enqueue(self, value):
        if self.isFull():
            raise ValueError("Queue is already full")
        else:
            if self.isEmpty():
                self.items[0] = value 
                self.start = 0 
                self.end = 0 
            else:
                self.items[self.end + 1] = value 
                self.end += 1
        
        
            
    def dequeue(self):
        if self.isEmpty():
            raise ValueError("Queue dosen't has any elements")
        else:
            if self.start == self.end:
                self.items = self.maxValu * [None]
                self.start = -1 
                self.end = -1
            else:
                self.items[self.start] = None
                self.start +=  1 
        
        if self.start != 0 and self.end == self.maxValu -1:
            self.end = -1  
            
    def delete(self):
        self.items = self.maxValu * [None]
        self.start = -1 
        self.end = -1
            
            
        
            
                
    

myQueue = CQUeue(4)
print(myQueue.isEmpty())
print(myQueue.isFull())
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.dequeue()
myQueue.dequeue()
myQueue.enqueue(5)
print(myQueue)
myQueue.delete()
print(myQueue)
