# Define Higher vs. Define Earlier #################################################
'''
def Bar():
    print("Bar")
    Baz()

def Foo():
    print("Foo")
    Bar()

def Main():
    print("Main")
    Foo()

def Baz():
    print("Baz")

Main()

def Baz():
    print("Baz")


print("All Done")
'''

# Doc String ###################################################################

def SomeMethod(arg1, arg2):
    '''
    Explain the method
    What are the args
    Usage of the method
    '''
    # Perform some tasks
    pass

# print(SomeMethod.__doc__)


# Return ######################################################################

def Method():
    x = 10
    y = 20

    return x, y

# a, b = Method()

# print(a, b)
# print(Method())


## Arguments to a Function ###################################################

def add(a, b, c=0):
    print(f"a --> {a}, b --> {b}, c --> {c}")
    return a + b + c

print(add(1, 2))        ## Positional argument
print(add(2, 1))

print(add(a = 1, b = 2))        ## Named argument / Key-worded args
print(add(b = 2, a = 1))

print(add(1, 2))                ## Default args
print(add(1, 2, 3))

#----- Variable, Keyworded Variable args ----------------------------------
