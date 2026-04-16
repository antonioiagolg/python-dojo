if __name__ == "__main__":
    size = int(input())
    stamps = set()

    for i in range(size):
        stamps.add(input())

    print(stamps)
    print(len(stamps))
