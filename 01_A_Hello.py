#!/usr/bin/env py

import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = 'there'

print ("Hello", name, "!")
print("Cmd args -->", sys.argv)

# py 01_Hello.py Ramakant
# ./01_Hello.py Manish    {requires the hashbang and executable permission (default provided in Windows)}
# IDE -  ctrl+ F5