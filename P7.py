from Utils import primes

def P7():
  p = primes(length = 10001)
  result = None
  for i in p:
    result = i
  return result

if __name__ == "__main__":
  print P7()
