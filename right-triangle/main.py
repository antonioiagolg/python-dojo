import math

if __name__ == "__main__":
    ab = int(input())
    bc = int(input())
    hypotenuse = math.sqrt(math.pow(ab, 2) + math.pow(bc, 2))
    angle = math.degrees(math.asin(ab / hypotenuse))
    result = round(angle)

    # The challenge asks to round 0.5 and following to the next integer
    # but the round function, in such situations round to the nearest even number
    # E.g.: 2.5 -> 2 instead of 3.
    # 3.5 -> 4
    # For the even numbers situation, we need to do a check and +1 to adhere with the
    # challenge requirement.
    if abs(result - angle) >= 0.5:
        result += 1
    print(f"{result}{chr(176)}")  # chr(176) means the degrees symbol
