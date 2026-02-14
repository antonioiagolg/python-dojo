# Triangle quest

The palidromic numbers we need to print have something in common: they are the result of another palindromic number in a power
of 2. For instance:

$$
1 = 1^2
121 = 11^2
12321 = 111^2
...
$$

So, the number of digits has a relation with the size of the triangle. So if the triangle has size 3, we should print in na loop like
the expression above. The trick part is that the challenge only accepts two lines: one for the for statement and another for the print.
No more fors allowed, neither string manipulation of any kind, not even a string literal is allowed.

The next step, taking the context, is to find a way to get the palindromic numbers 1, 11, 111, ... based on the iterable. Let's
try to represent these numbers using the base 10:

$$
1 != 10^0 + 1 (problem here)
11 = 10^1 + 1
111 = 10^2 + 1
...
$$

For the first loop, we can't use the above pattern, but we still can try to find the number using the base 10:

$$
1 = (10^1 - 1) / 9
11 = (10^2 - 1) / 9
111 = (10^3 - 1) / 9
...
$$

This pattern is suitable for our problem. We can find the palindromic numbers by using the expression inside the for loop. To make sure
we will have a integer number and not a float, we are going to use the // operator in python. The  final expression is:

$$
result = ((10^i - 1) / 9)^2 for 1 <= i <= size
$$
