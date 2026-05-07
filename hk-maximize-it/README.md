# Maximize it

- First I tried to find a way to identify the best element to be choosed in each array and generate the max result, but the maximized result is heavily dependent of all the numbers choosed, which means that I can decide the best, because it won be suitable for the best in the next array.

- One approach is to perform the cartesian product on the arrays, but I saw some comments that it is possible to do it without the itertools so I could sleep thinking about this XD. 

- Because of the nature of the problem, we still have to check every combination of choosed numbers, apply the function, sum and perform the modulus. One way we can do it is using a set to hold the partial sums and modulus of choosed numbers. The formula (A + B + C ... + N) mod Z is the same as the ((A mod Z) + (B mod Z) + ... (N mod Z)) mod Z. So, for each element in the array, we can apply the pow function, then calculate the modulus, sum with partial choosed elements from the set and calculate the modulus. Each element in the set corresponds to a combination of choosed elements from a cartesian product, but without having to generate the product.

- At the end, we just need to choose the maximun value from the set.
