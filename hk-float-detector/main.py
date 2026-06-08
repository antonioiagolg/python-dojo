#import re
test_cases = int(input())

for i in range(test_cases):
    num = input()
    if '.' not in num:  # execution time: 19 ms (faster approach)
        #if not re.search(r'\.', num): # execution time: 29ms
        print(False)
        continue
    try:
        num = float(num)
        print(True)
    except Exception as e:
        print(False)
