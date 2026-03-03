def average(arr):
    distinct_elements = set(arr)
    total = sum(distinct_elements)
    qtd = len(distinct_elements)

    if qtd == 0:
        return f"{result:.3f}"

    result = total / qtd
    return f"{result:.3f}"

if __name__ == "__main__":
    size = int(input())
    arr = list(map(int, input().split()))
    average(arr)
    result = average(arr)
    print(result)
