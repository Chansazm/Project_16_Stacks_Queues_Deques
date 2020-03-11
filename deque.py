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
        """return true when stack is empty"""
        return len(self.data) == 0

    def push(self, e):
        """Add an element to the end of the stack"""
        self.data.append(e)
