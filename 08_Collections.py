## Lists
# Collection of non-homogeneous objects


def add(a, b):
    return a + b

def Test1():
    print(type(add))

    lst1 = [1, 2, 3, "Ramakant", "Manish", "Abhijeet", add]
    print(lst1)
    print(lst1[6](3, 4))
    print("Ramakant" in lst1)
    for x in lst1:
        print(x, type(x))

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

def add(x, y, z):
    return x + y + z
    
# Sequence (Un)packing 
def Test7():
    lst = [1, 2, 3, 4, 5, 6]
    extras = []
    a, b, c, *extras = lst
    print(a, b, c, extras, sep='\n')

    print(add(extras[0], extras[1], extras[2]))
    print(add(*extras))

    print("Done")


## Dictionaries
def Test8():
    dt1 = {
        '1': "Python", 
        '2' : "Containers"
        }
    dt2 = dict({'A':10, 'B':20})
    print(dt1)
    print(dt2)

    st = {1, 2, 3, 4}
    dt3 = dict.fromkeys(st)
    print(dt3)

    fs1 = frozenset([1, 2, 3])
    tp = (1, 2, 3)
    print(type(fs1), hash(fs1))
    st2 = set([1, 2, 3, 4, 5, 1, 4, 5, fs1, tp])
    dt4 = dict.fromkeys(st2)

    print(dt4)

    for k in dt4.keys():
        print(k)
        
    for v in dt4.values():
        print(v)

    for k, v in dt4.items():
        print(f"{k} --> {v}")        

    print(dt2['A'])
    dt2['A'] = 100
    print(dt2['A'])

    dt2['C'] = 300
    print(dt2)

    if 'd' in dt2:
        print(dt2['D'])
    else:
        print("No such key")

    print("Value -->", dt2.get('C'))
    print("Value -->", dt2.get('D'))

    print("\n", '-'*40, '\n')
    dt2.update(dt4)
    print(dt2)

    print(dt2.pop('B'))
    print(dt2)

    print(dt2.popitem())
    print(dt2)

# Tuple - Like a list in almost all manner; Immutable
# Ordered, Can contain (im)mutables, Sliced, Indexed
def Test9():
    tp1 = tuple([1, 2, 3])
    tp2 = (1, 2, 3, 4)
    print(tp2[2])

    str1 = "This is a Python training in Pune for Engineers"
    lst = str1.split()
    print(lst)

    # Named tuples
    # [roll:int, name:str, age: int, GPA: int]
    lstStud = [1, 'Pravin', 17, 4]

    from collections import namedtuple
    Student = namedtuple('StudentCls', 'roll name age gpa')
    s1 = Student(1, "Abhijeet", 14, 4.2)
    s2 = Student(2, "Manish", 12, 4.3)

    print(f"Name --> {s1[1]}")
    print(f"Name --> {s1.name}")
    print(type(s1))

    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(10, 20)
    print(p1.x, p1.y)

# Comprehensions
def Test10():
    fruits = ['apple', 'banana', 'coconut', 'dragonfuit', 'elderberry', 'fig', 'guava','jackfruit', 'mango']

    '''
    newlist = []
    for fr in fruits:
        if 'a' in fr:
            newlist.append(fr)
    '''
    newlist = [    fr       for fr in fruits        if 'a' in fr    ]
    print(newlist)

    lst = [    fr                           for fr in fruits        if 'a' in fr    ]
    tp  = tuple(    fr                      for fr in fruits        if 'a' in fr    )
    st  = {    fr                           for fr in fruits        if 'a' in fr    }
    dt  = {    fr : fr.capitalize()         for fr in fruits        if 'a' in fr    }
    gn  = (    fr                           for fr in fruits        if 'a' in fr    )

    print(f"{type(lst)} --> {lst}")
    print(f"{type(tp)} --> {tp}")
    print(f"{type(st)} --> {st}")
    print(f"{type(dt)} --> {dt}")
    print(f"{type(gn)} --> {gn}")

def Test11():
    lst = [1]
    tp = (1,)
    st = {1}
    dt = {1:1}
    print(f"{type(lst)} --> {lst}")
    print(f"{type(tp)} --> {tp}")
    print(f"{type(st)} --> {st}")
    print(f"{type(dt)} --> {dt}")

def Test12():
    print(dir(str))
    # x = 10
    # print(dir(x))

    pubAttribs = [ attrib   for attrib in dir(str)    if attrib.startswith('_') is False]
    # add the condition that the attrib is callable --> __call__ is overridden
    print(pubAttribs)


Test12()