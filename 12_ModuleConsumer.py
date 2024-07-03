def Test1():
    from _12_Modules import greet
    greet()
    # greetName("Test")
    # greetInteractive()

def Test2():
    greet()
    greetName("Test")
    greetInteractive()


Test1()

from _12_Modules import *

Test2()

