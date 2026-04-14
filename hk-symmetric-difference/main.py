if __name__ == "__main__":
    size_m = int(input())
    m_raw = list(map(int, input().split()))
    size_n = int(input())
    n_raw = list(map(int, input().split()))

    set_m = set(m_raw)
    set_n = set(n_raw)

    a = set_m.difference(set_n)
    b = set_n.difference(set_m)
    result = sorted(list(a.union(b)))

    for i in result:
        print(i)
