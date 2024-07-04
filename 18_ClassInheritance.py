class A:
    def __init__(self) -> None:
        super().__init__()
        print("A.Init", self.__class__.__mro__, super())

class B:
    def __init__(self) -> None:
        super().__init__()
        print("B.Init", self.__class__.__mro__, super())

class C:
    def __init__(self) -> None:
        super().__init__()
        print("C.Init", self.__class__.__mro__, super())

class D(A, C, B):
    def __init__(self) -> None:
        super().__init__()
        print("D.Init", self.__class__.__mro__, super())


obj = D()

print("_"*40)

obj2 = A()