from Utils import isPalindrome

def P4():
  maxPalindrome = 0
  for i in range(111, 1000):
    for j in range(111, 1000):
      product = i * j
      if isPalindrome(product):
        maxPalindrome = max(maxPalindrome, product)
  return maxPalindrome

if __name__ == "__main__":
  print P4()
