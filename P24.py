from itertools import permutations

def P24():
  counter = 1
  for p in permutations(range(10)):
    if counter == 1000000:
      return int(''.join(str(x) for x in p))
    counter += 1

if __name__ == "__main__":
  print P24()
