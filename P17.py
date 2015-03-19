def P17():
  AND = 0

  words = {
      1:'one',
      2:'two',
      3:'three',
      4:'four',
      5:'five',
      6:'six',
      7:'seven',
      8:'eight',
      9:'nine',
      10:'ten',
      11:'eleven',
      12:'twelve',
      13:'thirteen',
      14:'fourteen',
      15:'fifteen',
      16:'sixteen',
      17:'seventeen',
      18:'eighteen',
      19:'nineteen',
      20:'twenty',
      30:'thirty',
      40:'forty',
      50:'fifty',
      60:'sixty',
      70:'seventy',
      80:'eighty',
      90:'ninety',
      100:'hundred',
      1000:'thousand',
      AND:'and'}

  # Uncommenting the commented out lines causes the program to print out the
  # English name of each number.
  numLetters = 0
  #w = ''
  for i in range(1, 1001):
    #print w
    #w = ''
    n = i
    if n == 1000:
      #w = w + words[1] + words[1000]
      numLetters += len(words[1]) + len(words[1000])
      continue
    if n >= 100:
      #w = w + words[n/100] + words[100]
      numLetters += len(words[n / 100]) + len(words[100])
      n %= 100
      if n != 0:
        #w = w + words[0]
        numLetters += len(words[AND])
      else:
        continue
    if n < 20:
      #w = w + words[n]
      numLetters += len(words[n])
      continue
    #w = w + words[(n / 10) * 10]
    numLetters += len(words[(n / 10) * 10])
    n %= 10
    if n != 0:
      #w = w + words[n]
      numLetters += len(words[n])

  #print w
  return numLetters

if __name__ == "__main__":
  print P17()
