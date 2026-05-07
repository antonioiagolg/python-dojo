def fn(x):
    return x * x

if __name__ == "__main__":
    size_and_modulus = list(map(int, input().split()))

    i_choosed_sums = {0}

    for i in range(size_and_modulus[0]):
        try:
            elements       = list(map(int, input().split()[1:]))
            elements       = list(map(fn, elements))
            elements       = list(map(lambda x: x % size_and_modulus[1], elements))
            i_choosed_sums = {(elem + i_partial_sum) % size_and_modulus[1] for elem in elements for i_partial_sum in i_choosed_sums}
        
        except Exception as e:
            print(f"Error: {e}")
            continue


    print(max(i_choosed_sums))



