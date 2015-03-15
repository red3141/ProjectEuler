from Utils import Fibonacci

def P2():
  total = 0
  fib = Fibonacci(maxValue = 4000000)
  for i in fib:
    if i % 2 == 0:
      total += i
  return total

print P2()
