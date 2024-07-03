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

# def add(a, b, c=0):
#     print(f"a --> {a}, b --> {b}, c --> {c}")
#     return a + b + c

# print(add(1, 2))        ## Positional argument
# print(add(2, 1))

# print(add(a = 1, b = 2))        ## Named argument / Key-worded args
# print(add(b = 2, a = 1))

# print(add(1, 2))                ## Default args
# print(add(1, 2, 3))

#----- Variable, Keyworded Variable args ----------------------------------

# lst = [1, 2, 3, 4, 5]
# a = lst
# a, b, c, *l1 = lst
# print(a, b, c, l1)

# lst = [1, 2, 3]

# def add(a, b, c):
#     return a + b + c

# print(add(*lst))

# def add2(*values):
#     print(type(values), values)
#     sum = 0
#     for value in values:
#         sum += val
#     return sum

# print(add2(5, 2, 1))
# print(add2(5, 2, 1, 7, 9))

# def PrintDetails(**kwArgs):
#     print(type(kwArgs), kwArgs)
#     for key, value in kwArgs.items():
#         print(f"{key} --> {value}")
#     print()

# PrintDetails(roll = 1, name = "Manish", age = 17)
# PrintDetails(roll = 2, name = "Vineet", age = 13)

# Special args - Enforcing Positional, Keyworded -----------------------------

# def PrintStudentDetails(roll, /, name, *, age, **kwArgs):
#     # Anything to the left of the '/' has to be a positional argument
#     # Anything to the right of the '*' has to be a key-worded argument
#     print(f"roll --> {roll}")
#     print(f"name --> {name}")
#     print(f"age --> {age}")

#     for key, value in kwArgs.items():
#         print(f"{key} --> {value}")
#     print()


# PrintStudentDetails(1, "Manish", age = 17)
# # PrintStudentDetails(1, "Manish", 17)
# PrintStudentDetails(2, name = "Vineet", age = 13)


# Using the argList (*vArgs, **kwArgs) -------------------------

def PrintDetails(*vArgs, **kwArgs):
    print(vArgs)
    print(kwArgs)
    for value in vArgs:
        print(value, end=' ')
    for value in kwArgs.values():
        print(value, end=' ')
    print()

# PrintDetails(1, 2, 3, 4)
# print()
# PrintDetails(1, 2, A=3, B=4)
# print()
# PrintDetails(C=1, D=2, A=3, B=4)

# def Wrap(fn):
#     def envelope(*vArgs, **kwArgs):         # Packing all that is received into vArgs and kwArgs
#         print("Calling", fn.__name__)
#         ret = fn(*vArgs, **kwArgs)           # Unpacking vArgs and kwArgs to get the data being passed 
#         print("Returned from", fn.__name__)
#         return ret
#     return envelope

# @Wrap
# def greetMe(name):
#     print("Hi", name, "!")

# @Wrap
# def add(a, b):
#     return a + b

# # greetMe = Wrap(greetMe)
# greetMe("Ramakant")

# # add = Wrap(add)
# print(add(2, 3))


# Scopes ------------------------------------

# LEGB - Local External Global Builtin

def Outer():
    # global s1
    s1 = "Outer String"
    def Inner():
        # nonlocal s1
        s1 = "Inner String"
        print("Inner -->", s1)
    Inner()
    print("Outer -->", s1)

    print("Globals -->", globals())
    print("Locals -->", locals())
    globals()['s1'] = "Modified String"

s1 = "Global String"

Outer()
print("Global -->", s1)