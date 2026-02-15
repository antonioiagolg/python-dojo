import sys
if __name__ == '__main__':
    thickness = int(input())
    if thickness % 2 == 0:
        print("should be odd")
        sys.exit(1)
    if thickness < 0 or thickness > 50:
        print("invalid thickness")
        sys.exit(1)
   
    for i in range(5):
        print(('H'*i).center(10, '-'))
