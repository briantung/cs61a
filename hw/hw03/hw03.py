def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <=3 :
        return n;
    elif n > 3 :
        return g(n-1)+2*g(n-2)+3*g(n-3);

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    return g(n);

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(10)
    False
    >>> has_seven(20)
    False
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k == 0 :
        return False

    if k <= 10 :
        return k % 7 == 0
    
    if has_seven(k%10) :
        return True
    else:
        return has_seven(k//10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"

    # i = 1
    # flag = 1
    # index = 1
    # while index < n:

    #     if index % 7 == 0 or has_seven(index):
    #         flag = -flag

    #     i += flag
    #     index += 1

    # return i

    def pingpong_num(x):

        if x <= 7:
            return x, 1
        else:
            result, flag_result = pingpong_num(x - 1)

        if (x-1) % 7 == 0 or has_seven(x-1):
            flag_result = - flag_result

        return result + flag_result, flag_result

    r, _ = pingpong_num(n)

    return r

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    
    def count(amount,coin):
        if amount == 0:
            return 1
        elif amount < 0:
            return 0
        elif coin > amount:
            return 0
        else:
            return count(amount-coin,coin) + count(amount,2*coin)

    return count(amount,1)



def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    
    def move(form,to):
        print("Move the top disk from rod %d to rod %d" % (form,to))

    if n == 1:
        move(start,end)
    else:
        other = 6 - start - end
        towers_of_hanoi(n-1, start, other)
        towers_of_hanoi(1, start, end)
        towers_of_hanoi(n-1, other, end)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """

    return (lambda f: lambda h: f(h, f))(lambda n, f: 1 if n == 1 else mul(n, f(sub(n, 1), f)))
