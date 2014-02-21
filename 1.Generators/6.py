#!/usr/bin/python3
import sys
import random


def main():
    rand = random.randrange(sys.maxsize)
    print("Sum for: ", rand, " iterations.")
    sums = sum(1 / 2 ** n for n in range(1, rand))
    print(sums)


if __name__ == "__main__":
    main()
