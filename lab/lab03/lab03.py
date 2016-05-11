# Q2
def make_buzzer(n):
    """ Returns a function that prints numbers in a specified
    range except those divisible by n.

    >>> i_hate_fives = make_buzzer(5)
    >>> i_hate_fives(10)
    Buzz!
    1
    2
    3
    4
    Buzz!
    6
    7
    8
    9
    """
    "*** YOUR CODE HERE ***"
    def buzz(range):
        r = 0;
        while r<range:
            if r%5 == 0 :
                print("Buzz!")
            else :
                print(r)
            r += 1 

    return buzz

# Q4
def f1():
    """
    >>> f1()
    3
    """
    "*** YOUR CODE HERE ***"
    l = lambda : 3
    print(l())


def f2():
    """
    >>> f2()()
    3
    """
    "*** YOUR CODE HERE ***"
    l = lambda : print(3)

    return l;

def f3():
    """
    >>> f3()(3)
    3
    """
    "*** YOUR CODE HERE ***"
    l = lambda x: print(x)
    return l
def f4():
    """
    >>> f4()()(3)()
    3
    """
    "*** YOUR CODE HERE ***"
    l = lambda :lambda x : lambda :print(x)
    return l
# Q6
def sum(n):
    """Computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    "*** YOUR CODE HERE ***"
    if(n==1):
        return 1
    else :
        return n + sum(n-1)

# Q7

def sum_every_other_number(n):
    """Return the sum of every other natural number 
    up to n, inclusive.

    >>> sum_every_other_number(8)
    20
    >>> sum_every_other_number(9)
    25
    """
    if n <= 0:
        return 0
    else:
        return n + sum_every_other_number(n - 2)


def fibonacci(n):
    """Return the nth fibonacci number.
    
    >>> fibonacci(11)
    89
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Q8
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if(n == 1):
        return 1
    elif(n%2==0):
        return hailstone(n//2)+1
    elif(n%2==1):
        return hailstone(n*3+1)+1