# Company Logo

- First we have to count the occurrences of each letter. I used a dict to hold letter and value.

- As we need to have the alphabetical order, I first sorted the items alphabetically, then I sorted it based on the occurrence count. The equal occurrences will keep ordered alphabetically, because the sorting methods are stable.

- Then I extraced the 3 most common letters and print them.

## References

- https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts
