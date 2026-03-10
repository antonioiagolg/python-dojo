import numpy

if __name__ == "__main__":
    coefficients = list(map(float, input().split()))
    x = float(input())

    print(numpy.polyval(coefficients, x))
