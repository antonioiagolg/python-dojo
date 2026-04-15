# Combinations

This challenge was trick, because I thought the result should be lexicographically ordered, but instead,
the combinations must be done based on the lexicographically ordered input. this matters when generating the
combination where the order does not matter. For example, for the input HACK, doing the combination without
sorting, would result in combinations like "HA" for 2 chosen caracteres. The combination "AH" would be skipped
because the "HA" was already created and the order does not matter.

Doing the combinations for the sorted ACHK, would result in the combination "AH", which is the expected result
from the challenge. Lessons learned: I need to check carefully the scope of the challenge.
