#############
# Iterators #
#############

class IteratorRestart:
    """
    >>> i = IteratorRestart(2, 7)
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.index = start - 1

    def __next__(self):
        if self.index == self.end:
            self.index = self.start - 1 
            raise StopIteration
        self.index += 1
        return self.index

    def __iter__(self):
        return self 

##############
# Generators #
##############

def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    while n >= 0:
        yield n
        n -= 1 

class Countdown:
    """
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        while self.n >= 0:
            yield self.n
            self.n -= 1 

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    i = n
    while i > 1:
        yield i
        if i % 2 == 0:
            i //= 2
        else:
            i = i * 3 + 1
    yield i


