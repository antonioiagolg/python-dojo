from itertools import permutations

if __name__ == "__main__":
    arg  = input().split(" ")
    word, size = sorted(arg[0]), int(arg[1])

    result = permutations(word, size)

    for elem in result:
        print("".join(elem))