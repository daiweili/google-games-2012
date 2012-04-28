import sys

def read_int():
    return int(sys.stdin.readline())

def read_float():
    return float(sys.stdin.readline())

def read_line():
    return sys.stdin.readline()

def read_lines(n=1):
    result = []
    for line in xrange(n):
        result.append(sys.stdin.readline())
    return result

def read_list(func=None):
    """Reads lists in the form:

    [number of elements]
    [element1] [element2] ... [elementn]

    Also applies the argument func to each element.
    """
    num = read_int()
    elems = read_line().split()

    if func is not None:
        elems = [func(x) for x in elems]
    return elems

if __name__ == '__main__':
    print read_list(int)
