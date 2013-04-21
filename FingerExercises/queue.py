class Queue(object):
    """represents a queue object"""
    def __init__(self):
        """ create an empty queue"""
        self.queue = []

    def insert(self, item):
        self.queue.append(item)

    def remove(self):
        if len(self.queue) == 0:
            raise ValueError

        retVal = self.queue[0]
        self.queue = self.queue[1:]
        return retVal



    
        
    
