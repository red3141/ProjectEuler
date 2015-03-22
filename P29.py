def P29():
  distinctPowers = {}
  for a in range(2, 101):
    for b in range(2, 101):
      x = a ** b
      if x not in distinctPowers:
        distinctPowers[x] = True
  return len(distinctPowers)

if __name__ == "__main__":
  print P29()
