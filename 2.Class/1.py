#!/usr/bin/python3
def func(*args):
    return ''.join([chr(i+96) for i in args])

def main():
    a = [7, 8]
    assert func(1, 2, 3) == "abc"
    assert func() == ""
    assert func(5, 6, *a) == "efgh"
    assert func(*a) == "gh"


if __name__ == "__main__":
    main()