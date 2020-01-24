from itertools import permutations
import string

perm = permutations(string.ascii_lowercase)
count = 0
for _ in list(perm):
    count += 1
print(count)