def rangoli(num: int) -> str:
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    lines = []
    for i in range(num):
        lines.append(get_line(alphabet[i:num]))

    upper_part = lines[:0:-1]
    width_line = len(lines[0])
    upper_part.extend(lines)

    result = ""
    for line in upper_part:
        result = result + f"{line:-^{width_line}}\n"
    
    return result

def get_line(range_letter):
    if len(range_letter) == 1:
        return range_letter[0]
    
    center_line = range_letter[0]
    for i in range(1, len(range_letter)):
        center_line = range_letter[i] + "-" + center_line + "-" + range_letter[i]

    return center_line

if __name__ == "__main__":
    number = int(input("Define a number: "))
    print(rangoli(number))