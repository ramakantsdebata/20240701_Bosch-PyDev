import decimal
import math

def round_it(x, ndigits, strategy=decimal.ROUND_HALF_UP):
    decimal.getcontext().rounding = strategy
    rounded = round(x, ndigits)
    print(f"round({x}, {ndigits}, {strategy}) --> {rounded}")

def Test1():
    x = decimal.Decimal('2.675')

    round_it(x, ndigits=2, strategy=decimal.ROUND_CEILING)      # Towards +inf
    round_it(x, ndigits=2, strategy=decimal.ROUND_FLOOR)        # Towards -inf
    round_it(x, ndigits=2, strategy=decimal.ROUND_UP)           # Away from '0'
    round_it(x, ndigits=2, strategy=decimal.ROUND_DOWN)         # Towards '0'
    round_it(x, ndigits=2, strategy=decimal.ROUND_HALF_UP)      # Ties away from '0'
    round_it(x, ndigits=2, strategy=decimal.ROUND_HALF_DOWN)    # Ties toward '0'
    round_it(x, ndigits=2, strategy=decimal.ROUND_HALF_EVEN)    # Ties towards the even
    round_it(x, ndigits=2, strategy=decimal.ROUND_05UP)         # Ties towas the nearest multiple of 0.05
    round_it(-x, ndigits=2, strategy=decimal.ROUND_CEILING)  
    round_it(-x, ndigits=2, strategy=decimal.ROUND_UP)


def Test2():
    # math.floor --> towards '-inf'
    print("math.floor(5.2) --> ", math.floor(5.2))
    print("math.floor(-5.2) --> ", math.floor(-5.2))
    print("")

    # math.ceil --> towards '+inf'
    print("math.ceil(5.2) --> ", math.ceil(5.2))
    print("math.ceil(-5.2) --> ", math.ceil(-5.2))
    print("")

    # math.trunc --> towards '0'
    print("math.trunc(5.2) --> ", math.trunc(5.2))
    print("math.trunc(-5.2) --> ", math.trunc(-5.2))
    print("")

    # round --> towards nearest integer
    print("round(5.2) --> ", round(5.2))
    print("round(-5.2) --> ", round(-5.2))
    print("round(5.7) --> ", round(5.7))
    print("round(-5.7) --> ", round(-5.7))
    print("round(5.5) --> ", round(5.5))
    print("round(-5.5) --> ", round(-5.5))
    print("")

Test1()