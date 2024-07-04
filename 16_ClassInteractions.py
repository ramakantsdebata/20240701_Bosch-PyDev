class Integer:
    def __init__(self, value) -> None:
        self.__val = int(value)
        self.x = 10

    def __str__(self) -> str:
        return f"[Integer -> {str(self.__val)}]"

    @property
    def value(self):
        return self.__val

    @value.setter
    def value(self, value):
        self.__val = value

def Test1():
    i1 = Integer(10)
    i1.value = 20
    print(i1)

    i2 = Integer(100)
    res = i1.value + i2.value
    print(res)
    print(i1.x)
    i1.__val = 200
    print("-->", i1.__val)
    print(i1) 
    print("-->", i1.__val)
    print(i1.__dict__)

def Test2():
    i1 = Integer(10)
    i2 = Integer(100)
    i3 = i1 + i2
    print(i3)

Test2()



# class Test:
#     def __init__(self) -> None:
#         self.__data = 12345

#     def check(self):
#         print(self.__data)

# t1 = Test()
# print(t1.__dict__)
# t1.check()
# t1._Test__data = 11111
# t1.check()