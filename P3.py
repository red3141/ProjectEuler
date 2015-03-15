from Utils import factor

def P3():
  toFactor = 600851475143
  factors = factor(toFactor, duplicates=False)
  maxFactor = 0
  for i in factors:
    maxFactor = max(maxFactor, i)
  return maxFactor

print P3()
