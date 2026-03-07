# Exceptions

This one was quite simple, the trick part is the way you receive the values. At first I was trying to perform the cast right after collecting the input, which made
the code output the exception error. Then, I changed the approach to receive firstthe values, then perform the cast and the division, appending the results or exceptions in an array. 
Other possible approach is to perform the cast right after receiving the value, and store the error in the result array. The objective is to show the result only at the end of the processing.
