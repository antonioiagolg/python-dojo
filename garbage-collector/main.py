import sys

print("Garbage collector===========================")

print("Reference count for mutable objects")
# Allocating memory to store the array
# and passing the reference to x
x = [1,2,3]

# As we are passing the reference x to the function,
# the function will print 2 which means:
# -> One reference from x
# -> One reference from the function
print(sys.getrefcount(x))

# y holds a reference to x, now x reference count is 2
y = x

# It will print 3:
# One reference from x
# One reference from the function
# One reference from the y
print(sys.getrefcount(x))

# The reference count is related to the object being referenced
# so when we print the refcount to y, it will be 3 as well
# meaning that the array is referenced three times, not the variable
print(sys.getrefcount(y))

print("Ref count for immutable objects")
z = "hello"

# For imutable objects, we might get different ref counts, because they may
# be used for other python modules, so in our script we are not actually create
# space in memory for them, some times we are just get a reference from python,
# it depends in how common is the imutable object through the entire Python
# environment
print(sys.getrefcount(z))
