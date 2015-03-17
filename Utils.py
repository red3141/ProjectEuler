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
    return

  if primesOnly:
    lastFactor = 0
    while n > 1:
      i = 2
      while n % i != 0:
        i += 1
      n /= i
    
      if duplicates:
        lastFactor = i
        yield i
      elif lastFactor != i:
        lastFactor = i
        yield i
      else:
        continue

  else:
    # Note: will not return n as a factor of n
    for i in range(1, n):
      if n % i == 0:
        yield i

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
