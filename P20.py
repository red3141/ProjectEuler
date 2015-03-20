from math import factorial
from Utils import sumOfDigits

def P20():
  return sumOfDigits(factorial(100))

if __name__ == "__main__":
  print P20()
