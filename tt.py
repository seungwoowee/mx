from itertools import permutations
from itertools import product

for i in permutations([1, 2, 3, 4], 2):
    print(i, end=" ")
print("\n")

for i in product([1, 2, 3], 'ab'):
    print(i, end=" ")
print("\n")

for i in product(range(3), range(3), range(3)):
    print(i, end=" ")
print("\n")

for i in product([1,2,3], repeat=2):
    print(i, end=" ")
