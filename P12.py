from Utils import numberOfFactors, triangle

def P12():
  i = 1
  while True:
    i += 1
    t = triangle(i)
    if numberOfFactors(t) > 500:
      return t

if __name__ == "__main__":
  print P12()
