from Utils import isPrime, primes

def P27():
  maxConsecutivePrimes = 0
  bestA = None
  bestB = None

  for a in range(-999, 1000):
    # For n^2 + an + b to be prime for n = 0, b must be prime.
    for b in primes(maxValue=1000):
      f = lambda x: x * x + a * x + b
      n = 0
      while isPrime(f(n)):
        n += 1
      if n > maxConsecutivePrimes:
        maxConsecutivePrimes = n
        bestA = a
        bestB = b
  return bestA * bestB

if __name__ == "__main__":
  print P27()
