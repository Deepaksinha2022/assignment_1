# Q8. Write a program to reverse a stack.

class Stack:
    
    def __init__(self,size):
        self.size = size
        self.stack = []
        
    def push(self,element):
        self.stack.append(element)
        
    def display(self):
        for i in self.stack:
            print(i)
    
    def reverse(self):
        for i in self.stack[::-1]:
            print(i)   
obj = Stack(5)
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)
obj.display()
obj.reverse()