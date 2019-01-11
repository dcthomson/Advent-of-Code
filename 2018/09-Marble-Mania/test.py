from itertools import cycle

lst = ['a', 'b', 'c']

pool = cycle(lst)

print pool[0]
