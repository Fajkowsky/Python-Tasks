#!/usr/bin/python3
def main():
    sums = sum(x**2 for x in range(1499) if not x % 7 and (x % 11) == 1)
    print(sums)


if __name__ == "__main__":
    main()