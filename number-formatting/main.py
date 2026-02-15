def print_formatted(number):
    width = len(f"{number:b}")

    for i in range(1, number + 1):
        print(f"{i:{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}")


if __name__ == "__main__":
    number = int(input("Number"))
    print_formatted(number)

