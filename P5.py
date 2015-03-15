from collections import defaultdict
from Utils import factor

def P5():
  primeFactorsOfAnswer = defaultdict(int)

  for i in range(1, 21):
    factors = factor(i)
    currentFactor = None
    currentFactorCount = 0
    for f in factors:
      if currentFactor is None or f != currentFactor:
        currentFactor = f
        currentFactorCount = 1
      else:
        currentFactorCount += 1

      primeFactorsOfAnswer[currentFactor] = max(
          primeFactorsOfAnswer[currentFactor], currentFactorCount)

  answer = 1
  for (primeFactor, primeFactorCount) in primeFactorsOfAnswer.items():
    answer *= (primeFactor ** primeFactorCount)

  return answer

if __name__ == "__main__":
  print P5()
