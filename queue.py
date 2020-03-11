class queue:
    def __init__(self):
        """create an empty stack"""
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)
        """add an item at the end of the queue, takes O(n)
        """
    # O(n)

    def dequeue(self):
        self.items.pop()
        """remove an item from the begining of the queue in O(1)
        """
    # O(1)

    def peek(self):
        if self.items:
            return self.items[-1]
        """return but do not remove the next item to be removed
        """

    def size(self):
        return len(self.items)
        """[summary]
        """

    def is_empty(self):
        return self.items == 0

    # todo: tests
    # *great work
    # ? need to do more

    # ***********************************************************
    # Tests


myq = queue()
myq.enqueue('8')
myq.enqueue('7')
myq.enqueue('6')
myq.enqueue('5')
myq.enqueue('4')
print(myq.peek())
print(myq.size())
print(myq.is_empty())
