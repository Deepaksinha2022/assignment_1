# Q.9 Write a program to find the smallest number using a stack

class Stack:
    
    def __init__(self):
        self.stack = []
        
    def push(self,element):
        self.stack.append(element)
        
    def display(self):
        for i in self.stack:
            print(i)

    def Max(self):
        max= self.stack[0]
        for i in self.stack:
            if i > max:
                max = i
        print("Maximum value in Stock is : ",max)
        

obj = Stack()
obj.push(2)
obj.push(15)
obj.push(0)
obj.display()
obj.Max()