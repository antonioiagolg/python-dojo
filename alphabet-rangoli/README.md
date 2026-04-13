# Rangoli

To solve this challenge, I decided the create a function to return the center line. For example, if we have n = 3, it means that the letter in the corners
will be "c". The left side and right side goes in the direction of the first letter in the alphabet, like the following:
```
c-b-a-b-c
```
The next iteration, I decrease the n and then I generate the center line. For n = 2, the center line would be:
```
c-b-c
```
At the end, I will have an array that contains the lines from the center til the end of rangoli.

To construct the upper part, I grab a slice, removing the first element of lines array, and I do a reverse on the slice. Next, we append the original
array to the reversed one, and we have the final result. We just ned to print the final array.
