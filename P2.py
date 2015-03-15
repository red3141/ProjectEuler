from Utils import fibonacci

def P2():
  total = 0
  fib = fibonacci(maxValue = 4000000)
  for i in fib:
    if i % 2 == 0:
      total += i
  return total

if __name__ == "__main__":
  print P2()
