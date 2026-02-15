from itertools import product
if __name__ == '__main__':
    first_tuple = [int(i) for i in input().split(" ")]
    second_tuple = [int(i) for i in input().split(" ")]
    first_tuple = sorted(first_tuple)
    second_tuple = sorted(second_tuple)

    for elem in list(product(first_tuple, second_tuple)):
        print(elem, end=" ")
    
    print()