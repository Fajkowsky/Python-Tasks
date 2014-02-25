#!/usr/bin/python3
from math import sin, cos

def main():
    my_list = [(sin(x), cos(y)) for x in range(49) for y in range(49)]
    print(my_list)


if __name__ == "__main__":
    main()
