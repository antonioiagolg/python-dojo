if __name__ == "__main__":
    N = input()
    integer_list = map(int, input().split())

    tu = tuple(list(integer_list))
    print(tu)
    print(hash(tu))

