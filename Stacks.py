
class ArrayStack:
    """LIFO stack implementation using a python list"""

    def __init__(self):
        """create an empty stack"""
        self.data = []

    def push(self,item):
        """Add an element to the end of the stack and do not return anything,time O(1)"""
        self.data.append(item)  

    def pop(self):
        """remove an element from the top of the stack"""
        if is_empty(self):
            raise Exception("Stack is empty")
        return self.data.pop()

    def __len__(self):
        """ return the number of elements in the stack"""
        return len(self.data)
    
    def is_empty(self):
        """return true if stack is empty"""
        return len(self.data) == 0

    def top(self):
        """return the element at the top but do not remove"""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data[-1]

#********************************************************************
#Tests

Stack = ArrayStack()
Stack.push(9)
Stack.push(2)
Stack.top()

Stack = [5,4,1,8, 2,8,9,7]
#Stack.sort()
temp = Stack[2]
print(temp)


