from math import factorial

def P34():
  # 9! = 362880
  # 9! * 8 = 2903040 < 10 ^ 7
  # Thus, no 8 digit number or longer can have a digit factorial sum with as
  # many digits as the number.
  # 9! * 7 = 2540160, so no 7 digit number greater than 2540160 can have a
  # digit factorial sum equal to the number.
  # Recall that 1 and 2 don't count.
  total = 0
  for i in range(3, 2540161):
    if sum(factorial(int(x)) for x in str(i)) == i:
      total += i
  return total

if __name__ == "__main__":
  print P34()
