## Lists
# Collection of non-homogeneous objects


def add(a, b):
    return a + b

def Test1():
    print(type(add))

    lst1 = [1, 2, 3, "Ramakant", "Manish", "Abhijeet", add]
    print(lst1)
    print(lst1[6](3, 4))

'''
int add(intx, int y)
{
    return x + y
}

typedef int (*fnType)(int, int)

fnType pFn = add
int res = fFn(1, 2)
'''

def Test2():
    lst1 = list((1, 2, 3, 4))
    print(lst1)

    lst2 = list(range(1, 20, 2))
    print(len(lst2))

    print(lst1)
    print(str(lst1))
    print(lst1.__str__())
    print(lst1.__repr__())

def Test3():
    class MyType:
        def __init__(self) -> None:
            self.x = 10
            self.y = 20
        
        def __str__(self):
            return f"x: {self.x}, y: {self.y}"
        
        def __repr__(self) -> str:
            return f"{id(self)} --> x[{self.x}], y[{self.y}]]"

    mt = MyType()
    print(mt)
    print(mt.__str__())
    print(mt.__repr__())

def Test4():
    lst1 = list(range(10))
    print(5 in lst1)

    lst2 = [1, 2, 1, 1, 3, 3, 4, 5, 2]
    print(lst2.count(1))

    print(max(lst2))
    print(min(lst2))
    print(sum(lst2))

def Test5():
    str1 = "Ramakant"
    str2 = str1
    
    str2 += "!!"
    print("Str1->", str1)
    print("Str2->", str2)

    print("="*40)

    lst1 = [1, 2, 3, 4, 5]
    # lst2 = lst1
    # lst2 = list(lst1)
    lst2 = lst1[:]


    lst2.append(6)
    print("lst1->", lst1)
    print("lst2->", lst2)


## Sets - Collection of keys
def Test6():
    st1 =set()
    st2 = set([1, 2, 3, 4, 5, 1, 4, 5])
    st3 = {1, 2, 3, 4, 5}

    print(type(st1), type(st2), type(st3), sep="\n")
    print(len(st1), len(st2), len(st3), sep="\n")

    print(hash("Test"))
    st4 = {"Test", "String", "Bosch", "Python"}
    print(st4)

    lst1 = list([1, 2, 3])
    lst1.append(st2)
    # print(hash(lst1))
    print(lst1)

    fst2 = frozenset(st2)
    print(type(fst2), fst2)
    st3.add(fst2)
    print(st3)

    print(st2.union(st3))
    print(st2 | st3)
    


# Sequence unpacking 

Test6()