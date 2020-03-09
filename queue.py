    def __init__(self):
        """create an empty stack"""
        self.data = []

    def enqueue(self,item):
        return self.data.insert(0,item)
