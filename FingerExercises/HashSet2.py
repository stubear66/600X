class hashSet(object):

    def __init__(self, numBuckets): 
        self.bucketList = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.bucketList.append([])

    def hashValue(self, e):

        if type(e) != int:
            raise ValueError

        return e % self.numBuckets

    def member(self, e):


        if type(e) != int:
            raise ValueError

        hashVal = self.hashValue(e)
        return e in self.bucketList[hashVal]
        