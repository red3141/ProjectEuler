from Utils import factor

def sumOfProperDivisors(n):
  factors = factor(n, primesOnly = False)
  # factor returns n as a factor of n, but n is not a proper divisor of n,
  # so pop it off.
  factors.pop()
  return sum(factors)

def P21():
  result = 0

  for i in range(1, 10000):
    s = sumOfProperDivisors(i)

    # If the sum of the proper divisors is less than i, then the sum will
    # have already been tested for amicability, so skip it.
    # If the sum of the proper divisors is equal to i, then i is a perfect
    # number, ie. it is a self-amicable number, which is not counted for this
    # problem.
    if s <= i:
      continue

    t = sumOfProperDivisors(s)

    if i == t:
      result += i
      if s < 10000:
        result += s

  return result

if __name__ == "__main__":
  print P21()
