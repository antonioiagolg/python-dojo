# Valid regex ?

* First I prepared the code to read the regexes from the STDIN. I need to find a way to check if the regex is valid.
Maybe the regex lib in python has the solution.

* The `re` package has a function to compile the regex and generate a Pattern object. If it is an invalid pattern, it raises
an error (PatternError). we could take advantage of this to print True or False, depending on the result of compilation, but...

* The newer python versions (3+) accept the regular expressions from the challenge, which are invalid, as valid regular expressions,
so we cannot use Python 3 to solve this. I switched to python 2, I adapted the code and it worked.

* I decided to keep the Python 2 version in the README and the code contains the version for Python 3.

```
import re

if __name__ == "__main__":
    total_regexes = int(input())
    regexes = []

    for i in range(total_regexes):
        regexes.append(raw_input())

    for regex_pattern in regexes:
        try:
            re.compile(regex_pattern)
            print "True"
        except Exception as e:
            print "False"
```
