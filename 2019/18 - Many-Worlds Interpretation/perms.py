# A Python program to print all  
# permutations using library function 
from itertools import permutations
import string
  
# Get all permutations of [1, 2, 3] 

# perm = permutations(list(string.ascii_lowercase), len(string.ascii_lowercase)) 

# # Print the obtained permutations 
# print(len(list(perm)))

A_LOWERCASE = ord('a')
ALPHABET_SIZE = 26


def _decompose(number):
    """Generate digits from `number` in base alphabet, least significants
    bits first.

    Since A is 1 rather than 0 in base alphabet, we are dealing with
    `number - 1` at each iteration to be able to extract the proper digits.
    """

    while number:
        number, remainder = divmod(number - 1, ALPHABET_SIZE)
        yield remainder


def base_10_to_alphabet(number):
    """Convert a decimal number to its base alphabet representation"""

    return ''.join(
            chr(A_LOWERCASE + part)
            for part in _decompose(number)
    )[::-1]


def base_alphabet_to_10(letters):
    """Convert an alphabet number to its decimal representation"""

    return sum(
            (ord(letter) - A_LOWERCASE + 1) * ALPHABET_SIZE**i
            for i, letter in enumerate(reversed(letters.upper()))
    )

alphabet = ""

low = 246244783208286292431866971536008152 # "aaaaaaaaaaaaaaaaaaaaaaaaaa"

# print(high - low)

# for i in range(low, int(high)):
#     # convert i to alpha 0-a, 1-b...P-z
#     print(i)

i = low - 1
percent = 0
while True:
    # newpercent = i / low * 100
    # roundedpercent = round(newpercent)
    # if roundedpercent > percent:
    #     percent = roundedpercent
    #     print(percent)

    alphabet = base_10_to_alphabet(i)

    i += 1

    if len(alphabet) != 26:
        continue

    print(alphabet)

    if alphabet == "abcdefghijklmnopqrstuvwxyz"
        print("alpha:", i)
        break

    if alphabet == "aaaaaaaaaaaaaaaaaaaaaaaaaa":
        print("a:", i)

    if alphabet == "zzzzzzzzzzzzzzzzzzzzzzzzzz":
        print("z:", i)
        break