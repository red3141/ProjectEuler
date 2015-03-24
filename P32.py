from itertools import permutations

def P32():
  toInt = lambda x : int(''.join(map(str, x)))

  pandigitalProducts = []

  # Cutting down on the number of cases to test:
  # For a * b = c:
  # Suppose c is 3 or fewer digits. Then a and b combined must be at least 6
  # digits. Then either a has more digits than c, b has more digits than c,
  # or both a and b have an equal number of digits to c. In all of these cases,
  # a * b > c.
  # Suppose c has 5 or more digits. Then a and b combined must have at most 4
  # digits. 10,000 > 999 * 9 > 99 * 99, and both of these are bigger than what
  # a * b could be, so it is guaranteed that a * b < c.
  # Thus, c is 4 digits.
  #
  # If a permutation exists that gives a * b = c, then a permutation exists
  # that gives b * a = c. We can thus require that for a * b = c, a is 1 or 2
  # digits, and b is 4 or 3 digits, respectively.

  for p in permutations(range(1, 10)):
    for i in range(1, 3):
      a = toInt(p[:i])
      b = toInt(p[i:5])
      c = toInt(p[5:])
      if a * b == c and c not in pandigitalProducts:
        pandigitalProducts.append(c)

  return sum(pandigitalProducts)

if __name__ == "__main__":
  print P32()
