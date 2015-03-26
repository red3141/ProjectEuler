from fractions import Fraction

def P33():
  product = Fraction(1, 1)

  for n in range(10, 99):
    for d in range(n + 1, 100):
      # Skip trivial examples of these types of fractions.
      if n % 10 == 0 and d % 10 == 0:
        continue

      f = Fraction(n, d)

      n1 = n / 10
      n2 = n % 10
      d1 = d / 10
      d2 = d % 10

      if (n1 == d1 and d2 != 0 and Fraction(n2, d2) == f or
          n1 == d2 and d1 != 0 and Fraction(n2, d1) == f or
          n2 == d1 and d2 != 0 and Fraction(n1, d2) == f or
          n2 == d2 and d1 != 0 and Fraction(n1, d1) == f):
        product *= f

  return product.denominator

if __name__ == "__main__":
  print P33()
