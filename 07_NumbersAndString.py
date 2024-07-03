def Test1():
    ## Numbers
    x = 10
    s1 = x.__str__()

    print(type(s1))

def test2():
    # Strings
    s1 = 'Test'
    s2 = "string"

    str1 = "This is Abhijeet's notebook."
    str2 = 'He said, "Thank you"'

    str3 = "First""Second"

    print(str1, str2)
    print(str3)

# This is a comment (Single line)

'''
Multiline comment
Triple quotes can be 
single quotes 
or 
double quotes
'''

def add(a: int, b: int)->int:
    '''
    This function returns the sum.
    Usage: add(<obj1>, <obj2>)-><obj>
    Ensure that the objects are integers only
    '''
    try:
        p = int(a)
        q = int(b)
    except ValueError:
        return add.__doc__      # doc string
    return p + q

def Test3():
    print("String addition -->", add("Test", "String"))
    print(add(1, 2))
    print(add('1', '2'))


def Test4():
    training = "Python"
    duration = 5
    print("This is a", training, "training for", duration, "days.")

    fmt1 = "This is a %s training for %d days."
    print(fmt1 % (training, duration))

    fmt2 = "This is a {} training for {} days"
    print(fmt2.format(training, duration))

    fmt3 = f"This is a {training} training for {duration} days"
    print(fmt3)

def Test5():
    # Slicing
    training = "Python"
    duration = 5
    str1 = f"This is a {training} training for {duration} days"
    # str1[ Start : Stop : Step ]
    print(str1[5:15])
    print(str1[5:])
    print(str1[:15])
    print(str1[-1])
    # print("-->", str1[-5:5:1])
    print(str1[-5:], str1[:5])
    print(str1[::2])
    print(str1[1::2])
    print(str1[::-1])

def Test6():
    training = "Python"
    duration = 5
    str1 = f"This is a {training} training for {duration} days"

    print(str1[-5:], str1[:5])
    print(str1[-5:5:-1])

def Test7():
    st1 = "ABCDEFGHI"
    print(st1[-1:5])
    print(st1[-1:], st1[:5], sep='')

def Test8():
    r1 = [1, 2, 3]
    r2 = [4, 5, 6]
    r3 = [7, 8, 9]
    mat = [r1, r2, r3]
    print(mat)

    # mat[1][2]
    row = mat[1]
    elem = row[2]
    print(elem)

    print(mat[1][2])

    mat[1][2] = 60

    for row in mat:
        for elem in row:
            print(elem, end=' ')
        print()

# Mutable class to hold an integer
class Integer:
    def __init__(self, value) -> None:
        self.val = int(value)

    def __str__(self) -> str:
        return str(self.val)
    
    def setVal(self, value):
        self.val = value

def Test9():
    r1 = (Integer(1), Integer(2), Integer(3))
    r2 = (Integer(4), Integer(5), Integer(6))
    r3 = (Integer(7), Integer(8), Integer(9))
    mat = (r1, r2, r3)
    print(mat[1][2])
    mat[1][2].setVal(60)

    for row in mat:
        for elem in row:
            print(elem, end=' ')
        print()


Test9()