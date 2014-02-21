#!/usr/bin/python3
import random
import sys


def end_of_loop():
    x = random.randrange(9)
    if not x == 7:
        return x
    raise StopIteration


def main():
    my_list = list(end_of_loop() for x in range(sys.maxsize))
    print(my_list)

if __name__ == "__main__":
    main()
