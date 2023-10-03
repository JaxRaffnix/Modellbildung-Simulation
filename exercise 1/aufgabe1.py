from math import ceil 
import numpy as np

# initial values for a,b,c
a=3
b = [2,3]

# c is a list of odd numbers from 1 to 77
MAX = 77
c = [0] * ceil(77 / 2)
odd_counter = 1
i = 0
while odd_counter <= 77:
    c[i] = odd_counter
    odd_counter += 2
    i += 1

#!! richtige lösung!
c = np.arange(1, 77+2, 2)

# write the values of b and c to a file
filename = "test.npz"
with open(filename, "w") as file:
    file.write(str(b) + "\n")
    file.write(str(c) + "\n")

# delete a, b and c
del(a,b,c)

with open(filename, "r") as input:
    b = input.readline()
    c = input.readline()

print(b,c)