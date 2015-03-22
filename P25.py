from Utils import fibonacci

def P25():
  fib = fibonacci()

  # The Utils.fibonnaci() generator only produces a single 1, but this problem
  # requires both to be considered, so start the counter at 1 instead of 0.
  counter = 1
  for f in fib:
    counter += 1
    if f >= 10 ** 999:
      return counter

if __name__ == "__main__":
  print P25()
