def P26():
  # For 1/d, d has a recurring cycle of length d-1 (this is not necessarily
  # the minimum length of the recurring cycle). Since we're looking at
  # d < 1000, 2500 digits should be plenty to contain any recurring cycle
  # at least twice.
  # By starting from d = 999 and going down, we can short circuit as soon as
  # a recurring cycle is found that is longer than all remaining d.

  longestCycle = 0
  bestD = 0
  for d in range(999, 0, -1):
    if longestCycle >= d:
      break

    # Use integers instead of floats because it's easier to get the digits
    # we need.
    q = str(10 ** 2500 / d)
    
    # Get past any digits before the recurring cycle starts
    while True:
      cycle = q[:d]
      if q.find(cycle, 1) != -1:
        break
      q = q[1:]

    cycleLength = q.find(cycle, 1)
    if cycleLength > longestCycle:
      longestCycle = cycleLength
      bestD = d

  return bestD

if __name__ == "__main__":
  print P26()
