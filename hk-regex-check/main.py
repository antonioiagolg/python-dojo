import re

if __name__ == "__main__":
    total_regexes = int(input())
    regexes = []

    for i in range(total_regexes):
        regexes.append(input())

    for regex_pattern in regexes:
        try:
            re.compile(r"{regex_pattern}")
            print("True")
        except error as e:
            print("False")
