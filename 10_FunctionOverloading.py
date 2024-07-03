from multipledispatch import dispatch

@dispatch(int, int)
def add(a, b):
    return a + b

@dispatch(int, int, int)
def add(a, b, c):
    return a + b + c

print(add(1, 2))
print(add(1, 2, 3))
