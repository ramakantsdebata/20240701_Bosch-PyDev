#!/usr/bin/env py

import sys

def add(a, b):
    return a + b

p = int(sys.argv[1])
q = int(sys.argv[2])

res = add(p, q)

print("Result -->", res)