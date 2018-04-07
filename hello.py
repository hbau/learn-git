import sys

if len(sys.argv) == 1:
    name = input("Please input your name: ")
else:
    name = sys.argv[1]

print("Hello " + name)