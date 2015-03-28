from Utils import isPrime, primes

def P35():
  circularPrimes = {}

  # Ignore primes with an even digit, because on of their circular variants
  # will be even, and hence, will not be prime. 2, of course, is the exception.
  for p in filter(lambda x: x == 2 or
                            ('0' not in str(x) and
                             '2' not in str(x) and
                             '4' not in str(x) and
                             '6' not in str(x) and
                             '8' not in str(x)), primes(maxValue = 1000000)):
    if p in circularPrimes:
      continue

    s = str(p)
    isCircularPrime = True
    circularNumbers = [p]
    for _ in range(len(s) - 1):
      s = s[len(s) - 1] + s[:len(s) - 1]
      circularNumbers.append(int(s))
      if not isPrime(int(s)):
        isCircularPrime = False
        break

    if isCircularPrime:
      for n in circularNumbers:
        circularPrimes[n] = True

  return len(circularPrimes)

if __name__ == "__main__":
  print P35()
