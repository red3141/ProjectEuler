from Utils import factor

def P23():
  abundantNumbers = {}
  # All integers greater than 28123 can be written as a sum of two abundant
  # numbers, so we don't need to find any abundant numbers greater than 28123.
  # We also know that 1 isn't abundant, so don't bother looking at that.
  for i in range(2, 28124):
    factors = factor(i, primesOnly=False)
    factors.pop()
    if sum(factors) > i:
      abundantNumbers[i] = True

  # It's easier to find the integers that are the sum of two abundant numbers
  # than it is to find those that aren't. So start with the sum of all the
  # possible numbers (1 to 28123), and subtract off the numbers that are the
  # sum of two abundant numbers.
  total = sum(range(1, 28124))
  for i in range(1, 28124):
    for j in abundantNumbers.keys():
      if i - j in abundantNumbers:
        total -= i
        break

  return total

if __name__ == "__main__":
  print P23()
