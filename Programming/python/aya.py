height = 8

A = [[" " for i in range(height)] for j in range(height)]
Y = [[" " for i in range(height)] for j in range(height)]

for row in range(height):
    for col in range(height):
        if ((col == 0 or col == height-2) and row != 0) or ((row == 0 or row == height//2) and (col > 0 and col < height-2)):
            A[row][col] = "*"

for row in range(height):
    for col in range(height):
        if (row == col and row < height // 2) or (row + col == height - 1 and row < height // 2) or (col == height // 2 and row >= height // 2):
            Y[row][col] = "*"

for i in range(height):
    for j in range(height):
        print(A[i][j], end="")
    print(end="  ")
    for j in range(height):
        print(Y[i][j], end="")
    print(end="  ")
    for j in range(height):
        print(A[i][j], end="")
    print(end="  ")
    print()