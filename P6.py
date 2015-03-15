def P6():
  sumOfSquares = sum([x * x for x in range(1, 101)])
  squareOfSum = sum(range(1, 101)) ** 2
  return abs(sumOfSquares - squareOfSum)

if __name__ == "__main__":
  print P6()
