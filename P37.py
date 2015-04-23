from Utils import isPrime

def P37():
  # Start at the first valid prime for this problem
  i = 11
  result = 0
  numFound = 0
  while True:
    if isPrime(i):
      s = str(i)
      isTruncatablePrime = True
      candidatesL = [s[x:] for x in range(1, len(s))]
      candidatesR = [s[:x] for x in range(1, len(s))]
      candidatesL.extend(candidatesR)
      for c in candidatesL:
        if not isPrime(int(c)):
          isTruncatablePrime = False
          break
      if isTruncatablePrime:
        result += i
        numFound += 1
        if numFound == 11:
          # We know there are only 11 such primes
          return result
    i += 1

if __name__ == "__main__":
  print P37()
