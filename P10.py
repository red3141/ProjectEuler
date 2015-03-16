from Utils import primes

def P10():
  return sum(primes(maxValue = 2000000))

if __name__ == "__main__":
  print P10()
