from datetime import datetime

def P19():
  numSundayTheFirsts = 0
  SUNDAY = 6
  for year in range(1901, 2001):
    for month in range(1, 13):
      if datetime(year, month, 1).weekday() == 6:
        numSundayTheFirsts += 1
  return numSundayTheFirsts

if __name__ == "__main__":
  print P19()
