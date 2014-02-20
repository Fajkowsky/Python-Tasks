#!/usr/bin/python3
def main():
    number_list = [-x for x in range(499) if not x%2 or x%3]
    print(number_list)


if __name__ == "__main__":
    main()