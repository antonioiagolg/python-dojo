if __name__ == "__main__":
    cases = int(input())
    tests = []
    result = []

    for i in range(cases):
        tests.append(input().split())

    for test in tests:
        try:
            a = int(test[0])
            b = int(test[1])

            result.append(f"{a//b}")
        except ValueError as e:
            result.append(f"Error code: {e}")
        except ZeroDivisionError as e:
            result.append(f"Error code: {e}")

    print("\n".join(result))

