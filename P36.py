from Utils import isPalindrome, numberToBase

def P36():
  return sum(x for x in range(1000000) if isPalindrome(x) and isPalindrome(numberToBase(x, 2)))

if __name__ == "__main__":
  print P36()
