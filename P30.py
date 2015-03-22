def P30():
  # 7 * (9 ** 5) < 1,000,000, so no number greater than 7 * (9 ** 5)
  # can be the sum of the powers of 5 of its digits.
  s = 0
  for i in range(2, 7 * (9 ** 5)):
    if i == sum(int(x) ** 5 for x in str(i)):
      s += i

  return s

if __name__ == "__main__":
  print P30()
