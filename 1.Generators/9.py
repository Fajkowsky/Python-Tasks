#!/usr/bin/python3
from math import sin, cos


def generate():
    my_list = [(sin(x), cos(y)) for x in range(49) for y in range(49)]
    return my_list


def main():
    my_dict = {int(item[0]*i): item[0] / item[1] for i, item in enumerate(generate())}
    print(my_dict)


if __name__ == "__main__":
    main()
