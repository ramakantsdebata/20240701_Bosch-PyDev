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

Test6()