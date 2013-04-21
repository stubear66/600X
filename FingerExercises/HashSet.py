class hashSet(object):

    def __init__(self, numBuckets):

        if type(numBuckets) != int or numBuckets <= 0:
            raise ValueError
   
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

    def insert(self, e):
        """
        e: an integer
        Inserts e into the appropriate hash bucket. Raises ValueError if e is not an integer.
        """
        if type(e) != int:
            raise ValueError

        if not self.member(e):
            hashVal = self.hashValue(e)
            self.bucketList[hashVal].append(e)

    def remove(self, e):
        if type(e) != int:
            raise ValueError
        if not self.member(e):
            raise ValueError

        hashVal = self.hashValue(e)
        bucket = self.bucketList[hashVal]
        bucket.remove(e)

    def getNumBuckets(self):
        return self.numBuckets

    def __str__(self):
        s = ''
        for i in range(self.numBuckets):
            s += 'Bucket: ' + str(i) + ' {' + str(self.bucketList[i]) + '}\n'

        return s
            
            

    







