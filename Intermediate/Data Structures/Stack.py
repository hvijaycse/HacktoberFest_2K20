from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
        
    #To add a value to stack
    def push(self, val):
        self.container.append(val)
    
    #To take out the last added value from stack
    def pop(self):
        return self.container.pop()
        
    #To know the first input value in Stack
    def peek(self):
        return self.container[-1]

    #To check if our Stack is empty
    def is_empty(self):
        return len(self.container) == 0
    
    #To get the length
    def size(self):
        return len(self.container)
    
    #To empty our Stack
    def empty_list(self):
        self.container.clear()
        
    #To reverse the order of Stack
    def reverse_order(self):
        self.container.reverse()
    
    #To print our Stack
    def print(self):
        print(self.container)
        
    def is_balanced(string):
        self.empty_list()
       
if __name__=='__main__': 
    stack = Stack()
    stack.push(1) #adds 1 to our Stack
    stack.push(2) #adds 2 to our Stack
    print(stack.pop()) #pops out value=2 from our Stack
    stack.print()
