def P15():
  # A 20x20 grid has 21 points along each edge, so we actually need a 21x21
  # array.
  grid = [[0] * 21 for _ in range(21)]

  for row in range(21):
    for column in range(21):
      if row == 0 or column == 0:
        grid[row][column] = 1
      else:
        grid[row][column] = grid[row - 1][column] + grid[row][column - 1]

  return grid[20][20]

if __name__ == "__main__":
  print P15()
