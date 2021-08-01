class deque:
    """Deque implementation using a python list"""

    def __init__(self):
        """create an empty deque"""
        self.items = []

    def add_front(self, item):
        """Add an element to the front of the deque"""
        return self.items.insert(0, item)

    def add_rear(self, item):
        """Add an element to the rear of the deque"""
        self.items.append(item)

    def remove_front(self):
        """remove an element from the front of the deque"""
        if self.items:
            self.items.pop(0)

    def remove_rear(self):
        """Add an element to the front of the deque"""
        if self.items:
            return self.items.pop()

    def peek_front(self):
        """check and return the next element to be removed from the front but do not remove
        """
        if self.items:
            return self.items[0]

    def peek_rear(self):
        """check and return the next elemt to be removed, if empty return error
        """
        if self.items:
            return self.items[-1]

    def __len__(self):
        """ return the number of elements in the deque"""
        return len(self.items)

    def is_empty(self):
        """return true when deque is empty"""
        return len(self.items) == 0
