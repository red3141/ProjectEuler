from operator import itemgetter

def P14():
  collatzLengths = [None] * 1000000
  
  # Starting from 999999 and going down will result in being able to skip
  # checking the Collatz sequence length for more numbers.
  for i in range(999999, 0, -1):
    if collatzLengths[i] is not None:
      continue

    collatzSequence = []
    n = i
    while n != 1:
      collatzSequence.append(n)
      if n % 2 == 0:
        n /= 2
      else:
        n = 3 * n + 1
    collatzSequence.append(1)

    # Store the length for the starting element of the sequence.
    # All other elements in the sequence will have a shorter Collatz length,
    # so mark that we don't need to check them.
    collatzLengths[i] = len(collatzSequence)
    for j in collatzSequence[1:]:
      if j < 1000000:
        # We only care about Collatz sequences starting at 1000000 or less.
        collatzLengths[j] = 0

  return (max(enumerate(collatzLengths), key=itemgetter(1)))[0]

if __name__ == "__main__":
  print P14()
