# XML depth

* This challenge can be solved with recursion. Every time we call the depth function for a child, we dig deeper in the node level.
At some point, the node has no children, then the core logic comes.

* If the level we are is greater than the maxdepth so far captured, we replace the maxdepth with the current level. We must have
this guard conditional to avoid the depth call stack to overwrite the maxdepth with lower levels as the function call "goes up".

* Once we are in the "surface" (no more recursion calls), we have captured the maxdepth. We can safely print it.
