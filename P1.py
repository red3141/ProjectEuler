# Problem 1

def problem1():
  total = 0
  for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
      total += i
  return total

print problem1()
