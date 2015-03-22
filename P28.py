def P28():
  s = 1
  counter = 1
  increment = 2
  while counter != 1001 ** 2:
    for _ in range(4):
      counter += increment
      s += counter
    increment += 2
  return s

if __name__ == "__main__":
  print P28()
