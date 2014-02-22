#!/usr/bin/python3


class Pizza(object):
    name = None
    size = 0.0

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return "{} - {}".format(self.name, self.size)


def main():
    names = ('ananas', 'papaja', 'margarita')
    sizes = (5, 10, 20)

    my_list = [Pizza(name, size) for name in names for size in sizes]
    print(my_list)


if __name__ == "__main__":
    main()
