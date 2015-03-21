import math

from collections import defaultdict

########## FIBONACCI ##########

def fibonacci(maxValue=None, length=None):
  a = 0
  b = 1
  if length is not None and maxValue is not None:
    print("Error! fibonacci: maxValue and length both not None!")
    return
  if length is None and maxValue is None:
    while True:
      b += a
      a = b - a
      yield b
  if maxValue is not None:
    while a + b <= maxValue:
      b += a
      a = b - a
      yield b
  else:
    for _ in range(length):
      b += a
      a = b - a
      yield b

########## FACTORING ##########

def factor(n, duplicates=True, primesOnly=True):
  if n < 1:
    return []

  sqrtn = int(math.sqrt(n))

  factors = []
  if primesOnly:
    while n > 1:
      f = None
      for i in range(2, sqrtn + 1):
        if n % i == 0:
          f = i
          break
      if f is None:
        f = n

      if duplicates or not factors or f != factors[-1]:
        factors.append(f)
      n /= f
    return factors

  else:
    if n == 1:
      return [1]

    primeFactors = factor(n)

    # Find the number of times each prime factor is repeated.
    primeFactorCounts = defaultdict(int)
    for p in primeFactors:
      primeFactorCounts[p] += 1

    # For each prime factor of n, find the powers of that prime that are
    # factors of n.
    listsOfPowersOfPrimeFactors = (
        [[prime ** i for i in range(count + 1)]
          for (prime, count) in primeFactorCounts.items()])

    # Select one prime power factor of n for each prime factor of n, and
    # multiply them together to get a factor of n. Except do all possibilities
    # of that.
    # It is guaranteed that no factor will be produced more than once, so the
    # result is a list of all factors of n.
    return sorted(
        reduce(lambda x, y: [a * b for a in x for b in y],
          listsOfPowersOfPrimeFactors))


def numberOfFactors(n):
  factors = factor(n)
  primeFactors = defaultdict(int)
  for f in factors:
    primeFactors[f] += 1

  if len(primeFactors.values()) == 0:
    return 1

  return reduce(lambda x, y : x*y, map(lambda x : x+1, primeFactors.values()))

########## IS PALINDROME ##########

def isPalindrome(n):
  digits = str(n)
  return digits == digits[::-1]

########## PRIME NUMBERS ##########

def isPrime(n):
  if n <= 1:
    return False
  if n == 2:
    return True
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def nextPrimeAfter(n):
  while True:
    n += 1
    if isPrime(n):
      return n

def primes(maxValue=None, length=None):
  if length is not None and maxValue is not None:
    print("Error! primes: maxValue and length both not None!")
    return

  nextPrime = 2
  if length is None and maxValue is None:
    while True:
      retVal = nextPrime
      nextPrime = nextPrimeAfter(nextPrime)
      yield retVal
  if maxValue is not None:
    while nextPrime <= maxValue:
      retVal = nextPrime
      nextPrime = nextPrimeAfter(nextPrime)
      yield retVal
  else:
    for _ in range(length):
      retVal = nextPrime
      nextPrime = nextPrimeAfter(nextPrime)
      yield retVal

########## READING IN GRID OF NUMBERS ##########

# integers is a string containing a sequence of ints separated by spaces
# This function does not check that grid contains a multiple of width
# integers.
def readIntegerGrid(integers, width):
  intList = [int(x) for x in integers.split()]
  return [intList[i:i + width] for i in range(0, len(intList), width)]

########## TRIANGLE NUMBERS ##########

def triangle(n):
  return (n * (n + 1)) / 2

########## READING IN TRIANGLE OF NUMBERS ##########

# integers is a string containing a sequence of ints separated by spaces
# This function does not check that the number of integers is a triangle
# number.
# The result is an array of arrays, where each element of the outer array
# has length (index + 1).
def readIntegerTriangle(integers):
  intList = [int(x) for x in integers.split()]
  result = []
  counter = 1
  while intList:
    result.append(intList[:counter])
    intList = intList[counter:]
    counter += 1
  return result

########## SUM OF DIGITS ##########

def sumOfDigits(n):
  return sum(int(x) for x in str(n))
