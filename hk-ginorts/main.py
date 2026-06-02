from itertools import groupby

def sort_asc_odd_first(elem):
    """
    returns the char code of the elem, but for the challenge purpose
    it makes the odd numbers to be the first, by subtracting their char code by 10
    so for the sorting function they will be considered the first in the ordering.
    """
    char_at = ord(elem)
    if char_at < 48 or char_at > 57: # not in number code range
        return char_at
    if char_at % 2 == 0:
        return char_at
    return char_at - 10

def groupby_asc(elem):
    """
    returns a index group based on the conditions:
    if the elem is in the number range -> return 2
    if the elem is in the uppercase letter range -> return 1
    if the elem is in the lowercase range -> return 0
    These groups will be later used to sort the groups for the challenge (first lowercase, then uppercase and last the numbers)
    """
    char_at = ord(elem)
    if char_at >= 48 and char_at <= 57:
        return 2
    elif char_at >= 65 and char_at <= 90:
        return 1
    elif char_at >= 97 and char_at <= 122:
        return 0
    else:
        return 9 # just not to break, and move all the out of scope chars to the end if it happens

word = input()
sorted_word = sorted(word, key=sort_asc_odd_first)

groups = []

for key, group in groupby(sorted_word, key=groupby_asc):
    groups.append((k, list(g)))

groups = sorted(groups, lambda x: x[0])

result = ""
for group in groups:
    result = result + "".join(group[1])

print(result)
