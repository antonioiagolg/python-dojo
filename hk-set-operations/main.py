if __name__ == "__main__":
    size_set = int(input())

    elements = list(map(int, input().split()))
    elem_set = set(elements)

    num_operations = int(input())
    for i in range(num_operations):
        operation_info = input().split()
        command = operation_info[0]
        
        if command == "pop":
            elem_set.pop()
        elif command == "remove":
            try:
                elem_set.remove(int(operation_info[1]))
            except KeyError as e:
                continue
        elif command == "discard":
            elem_set.discard(int(operation_info[1]))
        else:
            continue

    print(sum(elem_set))
