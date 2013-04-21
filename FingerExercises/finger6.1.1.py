def thisRaisesAZeroDivisionError():
    x = 1/0

def thisRaisesAValueError():
    y = int('Five')

def thisDoesNotRaiseAnyErrors():
    z = 'just a string'

def tryExercise():
    print 'A',
    try:
        # Line Of Code Is Inserted Here #
        return
        print 'B',
    except ZeroDivisionError as e:
        print 'C',
    else:
        print 'D',
    finally:
        print 'E',
    print 'F'


def isPrime(n):
    if n <= 0:
        raise ValueError
    elif type(n) <> int:
        raise TypeError
    if n == 1 or n == 2:
        return True
    i = n/2 + 1
    for j in range(2,i):
        if n % j == 0:
            return False
    return True

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print self.time

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        return "Coordinate(" + str(self.getX()) + ", " + str(self.getY()) + ")"
    

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def __len__(self):
        return len(self.vals)

    def intersect(self, other):
        """Returns the intersection of 2 intSets as an intSet"""
        intersection = intSet()
        for i in self.vals:
            if other.member(i):
                intersection.insert(i)
        return intersection

    

