def print_arrow_up(thickness):
    for i in range(thickness):
        c = 'H'
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness-1))

def print_arrow_down(thickness):
    for i in range(thickness):
        c = 'H'
        print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))


def print_two_pillars(thickness):
    for i in range(thickness+1):
        c = 'H'
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

def print_cross_line(thickness):
    for i in range((thickness+1)//2):
        c = 'H'
        print((c * thickness * 5).center(thickness * 6))

if __name__ == '__main__':
    thickness = int(input('The thickenss: '))
    print_arrow_up(thickness)
    print_two_pillars(thickness)
    print_cross_line(thickness)
    print_two_pillars(thickness)
    print_arrow_down(thickness)


