## 1. Use immutable types ########################################################################
my_tuple = (1, 2, 3) 
try:
    my_tuple[0] = 4 
except TypeError as ex:
    print(repr(ex))


## 2. Encapsulate with Class ########################################################################
class MyClass: 
    def __init__(self, value): 
        self.__value = value # Private variable 

    @property 
    def value(self): 
        return self.__value 

    def do_something(self): 
        # Some operations 
        pass 

obj = MyClass(42) 
print(obj.value) # Access the value 
obj.__value = 100 # Modifying _value (not recommended) 
print(obj.value) # Access the value again 


## 3. Use Constants ########################################################################

MY_CONSTANT = 42 

## 4. Freezing Objects ########################################################################
fs1 = frozenset([1, 2, 3])

try:
    fs1.add(4)
except AttributeError as ex:
    print(repr(ex))


## 5. Use third-party libraries ########################################################################

import attr
@attr.s(frozen=True) 
class Point: 
    x = attr.ib() 
    y = attr.ib() 

point = Point(1, 2) 
# Attempting to modify attributes will raise an error 
try:
    point.x = 10 # Raises attr.exceptions.FrozenInstanceError: cannot assign to field 'x' 
except attr.exceptions.FrozenInstanceError as ex:
    print(repr(ex))