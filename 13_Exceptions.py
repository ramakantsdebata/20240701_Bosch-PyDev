def Foo():
    x = 10
    y = 0
    raise ZeroDivisionError("Denominator is zero")
    res = x/y
    return res

def Bar():
    print("Bar")
    try:
        Foo()
    except Exception:
        print("Had an exception, Not sure which")
        raise

    print("Returning from Foo")

def Main():
    print("Main")
    try:
        Bar()
    except ZeroDivisionError as ex:
        print(f"Is a ZeroDivisionError - {ex!r}")
    except (TypeError, ValueError) as ex:
        print(f"Is a Type/Value Error - {ex!r}")
    except Exception as ex:
        print(f"Some exception raised - {ex!r}")

    print("Returning from Bar")

Main()
