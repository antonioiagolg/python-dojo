def print_triangle_number(size: int):
    for i in range(size):
        print(((10**i - 1) // 9) ** 2)


# 10 - 1 = 9

# 9 / 9 = 1

# 1

# 100 - 1 = 99
# 99 / 9 = 11

# 121

# 1000 - 1 = 999
# 999 // 9 = 111

# 12321

if __name__ == "__main__":
    size = int(input())
    print_triangle_number(size)
