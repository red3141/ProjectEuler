def P31():
  coins = (1, 2, 5, 10, 20, 50, 100, 200)
  numberOfCoinSums = [0] * 201
  numberOfCoinSums[0] = 1

  for c in coins:
    for i in range(1, 201):
      if i - c >= 0:
        numberOfCoinSums[i] += numberOfCoinSums[i - c]

  return numberOfCoinSums[-1]

if __name__ == "__main__":
  print P31()
