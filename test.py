from Utils import *

def infiniteFibonacciTest():
  expected = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

  fib = fibonacci()
  actual = []
  counter = 0
  for i in fib:
    actual.append(i)
    counter += 1
    if counter == len(expected):
      break

  if actual != expected:
    print "ERROR: infiniteFibonacciTest FAILED!"

def lengthFibonacciTest():
  expected = [1, 2, 3, 5, 8, 13, 21]

  fib = fibonacci(length = len(expected))
  actual = []
  for i in fib:
    actual.append(i)
  
  if actual != expected:
    print "ERROR: lengthFibonacciTest FAILED!"

def maxValueFibonacciTest():
  expected = [1, 2, 3, 5, 8, 13]

  fib = fibonacci(maxValue = 13)
  actual = []
  for i in fib:
    actual.append(i)

  if actual != expected:
    print "ERROR: maxValueFibonacciTest FAILED!"

def primeFactorsDuplicatesTest():
  expected = [3, 3, 5, 5]

  factors = factor(225)
  actual = []
  for i in factors:
    actual.append(i)

  if actual != expected:
    print "ERROR: primeFactorsDuplicatesTest FAILED!"

def primeFactorsNoDuplicatesTest():
  expected = [3, 5]

  factors = factor(225, duplicates = False)
  actual = []
  for i in factors:
    actual.append(i)

  if actual != expected:
    print "ERROR: primeFactorsNoDuplicatesTest FAILED!"

def allFactorsTest():
  expected = [1, 3, 5, 9, 15, 25, 45, 75]

  factors = factor(225, primesOnly = False)
  actual = []
  for i in factors:
    actual.append(i)

  if actual != expected:
    print "ERROR: allFactorsTest FAILED!"

def isNotPalindromeTest():
  if isPalindrome("1234567890"):
    print "ERROR: isNotPalindromeTest FAILED!"

def isPalindromeEvenLengthTest():
  if not isPalindrome("12345678900987654321"):
    print "ERROR: isPalindromeEvenLengthTest FAILED!"

def isPalindromeOddLengthTest():
  if not isPalindrome("1234567890987654321"):
    print "ERROR: isPalindromeOddLengthTest FAILED!"

def isNotPrimeTest1():
  if isPrime(91):
    print "ERROR: isNotPrimeTest1 FAILED!"

def isNotPrimeTest2():
  if isPrime(1):
    print "ERROR: isNotPrimeTest2 FAILED!"

def isPrimeTest1():
  if not isPrime(2):
    print "ERROR: isPrimeTest1 FAILED!"

def isPrimeTest2():
  if not isPrime(97):
    print "ERROR: isPrimeTest2 FAILED!"

def nextPrimeAfterTest():
  if nextPrimeAfter(5) != 7:
    print "ERROR: nextPrimeAfterTest FAILED!"

def infinitePrimesTest():
  expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

  p = primes()
  actual = []
  counter = 0
  for i in p:
    actual.append(i)
    counter += 1
    if counter == len(expected):
      break

  if actual != expected:
    print "ERROR: infinitePrimesTest FAILED!"

def lengthPrimesTest():
  expected = [2, 3, 5, 7, 11, 13, 17]

  p = primes(length = len(expected))
  actual = []
  for i in p:
    actual.append(i)
  
  if actual != expected:
    print "ERROR: lengthPrimesTest FAILED!"

def maxValuePrimesTest():
  expected = [2, 3, 5, 7]

  p = primes(maxValue = 7)
  actual = []
  for i in p:
    actual.append(i)

  if actual != expected:
    print "ERROR: maxValuePrimesTest FAILED!"

def readIntegerGridTest():
  expected = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 0],
              [9, 8, 7, 6, 5]]
  actual = readIntegerGrid("1 2 3 4 5 6 7 8 9 0 9 8 7 6 5", 5)
  if actual != expected:
    print "ERROR: readIntegerGridTest FAILED!"



if __name__ == "__main__":
  infiniteFibonacciTest()
  lengthFibonacciTest()
  maxValueFibonacciTest()
  primeFactorsDuplicatesTest()
  primeFactorsNoDuplicatesTest()
  allFactorsTest()
  isNotPalindromeTest()
  isPalindromeEvenLengthTest()
  isPalindromeOddLengthTest()
  isNotPrimeTest1()
  isNotPrimeTest2()
  isPrimeTest1()
  isPrimeTest2()
  nextPrimeAfterTest()
  infinitePrimesTest()
  lengthPrimesTest()
  maxValuePrimesTest()
  readIntegerGridTest()
