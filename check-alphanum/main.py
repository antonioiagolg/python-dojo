if __name__ == '__main__':
    s = input()
    has_alphanum = False
    has_alpha = False
    has_num = False
    has_lower = False
    has_upper = False

    for i in s:
        if i.isalpha():
            has_alpha = True
        if i.isdigit():
            has_num = True
        if i.islower():
            has_lower = True
        if i.isupper():
            has_upper = True

    has_alphanum = has_alpha or has_num

    print(has_alphanum)
    print(has_alpha)
    print(has_num)
    print(has_lower)
    print(has_upper)
