def fibonacci(maxValue=None, length=None):
  a = 0
  b = 1
  if length is not None and maxValue is not None:
    print("Error! fibonacci: maxValue and length both not None!")
    return
  if length is None and maxValue is None:
    while True:
      b += a
      a = b - a
      yield b
  if maxValue is not None:
    while a + b <= maxValue:
      b += a
      a = b - a
      yield b
  else:
    for _ in range(length):
      b += a
      a = b - a
      yield b

def factor(n, duplicates=True):
  lastFactor = 0
  while n > 1:
    i = 2
    while n % i != 0:
      i += 1
    n /= i
    
    if duplicates:
      lastFactor = i
      yield i
    elif lastFactor != i:
      lastFactor = i
      yield i
    else:
      continue
