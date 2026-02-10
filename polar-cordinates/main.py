import cmath

if __name__ == "__main__":
    complex_number = complex(input())
    r = abs(complex_number)
    phase = cmath.phase(complex_number)
    print(r)
    print(phase)
