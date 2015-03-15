def Fibonacci(maxValue=None, length=None):
  a = 0
  b = 1
  if length is None and maxValue is None:
    print("Error! Fibonacci: maxValue and length both None!")
    return
  if length is not None and maxValue is not None:
    print("Error! Fibonacci: maxValue and length both not None!")
    return
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
