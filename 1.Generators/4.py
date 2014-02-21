#!/usr/bin/python3
def main():
    my_tuple = ("krzysiu", "socek", "faja", "wyplata")
    my_dict = {key.upper(): len(key) for key in my_tuple}
    print(my_dict)

if __name__ == "__main__":
    main()