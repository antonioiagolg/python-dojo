# Solution description

To have the sorted permutations, we need first to sort the input word. After creating the permutations, there is a little trick here:
The output expected a word-like variable, but the permutation function returns a sequence of tuples, each tuple determined by the size passed
to the permutation. Before printing, I transformed each tuple in a string using the join function to reach the desired output.