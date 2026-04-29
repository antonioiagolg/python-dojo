# Piling Numbers

- First I tried with recursion, poping the righest cubes from the deque, but I reached RecursionError (max limit 1000)

- I followed the iterable approach. First I check what box is the largest from both ends of the deck, them I put back the smallest one, and I keep the
largest as the "ground" for the next box. The ground variable is initialized with a value bigger than the scope of the boxes, so for sure all boxes from
the deque will be able to stack on the ground.
