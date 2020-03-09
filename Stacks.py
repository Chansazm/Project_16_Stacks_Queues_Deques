class Empty(Exception):
    """Error attempting to access from an empty container."""
    pass

class ArrayStack:
    """LIFO stack implementation using a python list"""

    def __init__(self):
        """create an empty stack"""
        self.data = []

    def __len__(self):
        """ return the number of elements in the stack"""
        return len(self.data)
    
    def is_empty(self):
        """return true if stack is empty"""
        return len(self.data) == 0:

    def push(self,e):
        """Add an element to the end of the stack"""
        self.data.append(e)
    
    def top(self):
        """return the element at the top but do not remove"""
        if self.data is_empty():
            raise Empty("Stack is empty")
        return self.data[-1]
    
    def pop(self):
        """remove an element from the top of the stack"""
        if is_empty(self):
            raise Exception("Stack is empty")
        return self.data.pop()




    def reverse_file(filename):
        S = ArrayStack()
        original = open(filename)
        for line in original:
        S.push(line.rstrip('\n')
        original.close()


        """Overwrite with contents in LIFO order"""
        """reopen the file and write"""
        output = open(filename,'w')
        while not S.is_empty():

            output.write(S.pop() + '\n')
            output.close()


    


