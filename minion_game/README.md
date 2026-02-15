# Solution description

Compute all substrings would be inefficient and time consuming. The substrings does not need to be combinations. The substrings
will be always the current letter in the world, plus the addition of the subsequent letters until the end of the word. For example:
```
BANANA
```
The substrings that starts with 'B' will be the letter B plus the subsequent letters until we reach the end of the word:
```
B
BA
BAN
BANA
BANAN
BANANA
```
Hence, taking into consideration that the letter 'B' is in the index 0, the total of the substrings starting from 'B' is the len(word) - index.
The algorithm will run in O(n).