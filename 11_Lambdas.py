# Lambda - Also known as Annonymous function in some texts

def Sort(coll, isGreater):
    for x in range(len(coll) - 1):
        for y in range(1, len(coll)):
            if isGreater(coll[x], coll[y]):
                print("Greater")
            else:
                print("Lesser")

##################################################################
## Much later

class Integer:
    def __init__(self, value) -> None:
        self.val = int(value)

    def __str__(self) -> str:
        return str(self.val)
    
    def setVal(self, value):
        self.val = value


def cmp(a: Integer, b: Integer)->bool:
    if a.val > b.val:
        return True
    return False

fn = lambda a, b: True if a.val > b.val else False

data = (Integer(7), Integer(8), Integer(9), Integer(4), Integer(5), Integer(6), Integer(1), Integer(2), Integer(3))

# Sort(data, cmp)
# Sort(data, fn)
Sort(data, lambda a, b: True if a.val > b.val else False)

# sq = lambda val : val ** 2
# print(sq(7))

tools = []
tools.append(lambda val : val ** 2)
tools.append(lambda val : val ** 3)

print(tools[0](7))

print(type(tools[0]))
print(type(Sort))

print(tools[0])
print(dir(tools[0]))
