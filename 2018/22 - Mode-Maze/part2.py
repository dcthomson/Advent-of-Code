import re
import collections

input_lines = []
with open("input.txt", 'r') as f:
    for line in f:
        line = line.strip()
        input_lines.append(line)

a,b = map(int, [re.findall('\d+', input_lines[i])[1] for i in [22, 24]])
number_to_factorize = 10551236 + a * 22 + b

factors = collections.defaultdict(lambda: 0)
possible_prime_divisor = 2
while possible_prime_divisor ** 2 <= number_to_factorize:
  while number_to_factorize % possible_prime_divisor == 0:
    number_to_factorize /= possible_prime_divisor
    factors[possible_prime_divisor] += 1
  possible_prime_divisor += 1
if number_to_factorize > 1:
  factors[number_to_factorize] += 1

sum_of_divisors = 1
for prime_factor in factors:
  sum_of_divisors *= (prime_factor ** (factors[prime_factor] + 1) - 1) / (prime_factor - 1)

print(sum_of_divisors)