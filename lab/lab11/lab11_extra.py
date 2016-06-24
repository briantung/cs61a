from lab11 import * 

###########
# Streams #
###########

class Stream:
    class empty:
        def __repr__(self):
            return 'Stream.empty'

    empty = empty()

    def __init__(self, first, compute_rest=lambda: Stream.empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

def make_integer_stream(first=1):
    def compute_rest():
        return make_integer_stream(first+1)
    return Stream(first, compute_rest)

def add_streams(s1, s2):
    """Returns a stream that is the sum of s1 and s2.

    >>> stream1 = make_integer_stream()
    >>> stream2 = make_integer_stream(9)
    >>> added = add_streams(stream1, stream2)
    >>> added.first
    10
    >>> added.rest.first
    12
    >>> added.rest.rest.first
    14
    """
    def add_s():
        return add_streams(s1.rest,s2.rest)

    return Stream(s1.first + s2.first, add_s)

def make_fib_stream():
    """Return a stream containing the Fib sequence.

    >>> fib = make_fib_stream()
    >>> fib.first 
    0
    >>> fib.rest.first
    1
    >>> fib.rest.rest.rest.rest.first
    3
    """

    def fib(n):
        if n == 0 or n==1:
            return n
        return fib(n-1) + fib(n-2)
        
    def make_fib(first):
        return Stream(fib(first),lambda:make_fib(first+1))  

    return make_fib(0) 

def filter_stream(filter_func, stream):
    def make_filtered_rest():
        return filter_stream(filter_func, stream.rest)
    if Stream.empty:
        return stream
    elif filter_func(stream.first):
        return Stream(stream.first, make_filtered_rest)
    else:
        return filter_stream(filter_funct, stream.rest)

def interleave(stream1, stream2):
    """Return a stream with alternating values from stream1 and stream2.

    >>> ints = make_integer_stream(1)
    >>> fib = make_fib_stream()
    >>> alternating = interleave(ints, fib)
    >>> alternating.first
    1
    >>> alternating.rest.first
    0
    >>> alternating.rest.rest.first
    2
    >>> alternating.rest.rest.rest.first
    1
    """     
    def make_interleave():
        return interleave(stream2,stream1.rest) 

    return Stream(stream1.first,make_interleave) 
