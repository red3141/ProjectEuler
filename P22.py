def P22():
  with open('res/P22Names.txt', 'r') as f:
    names = sorted(f.read().translate(None, '\"').split(','))
    total = 0
    for (index, name) in enumerate(names, start=1):
      alphabeticalValue = sum((ord(x) - ord('A') + 1) for x in name)
      total += index * alphabeticalValue
    return total

if __name__ == "__main__":
  print P22()
