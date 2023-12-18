height = 8
M = [[" " for i in range(height)] for j in range(height)]
A = [[" " for i in range(height)] for j in range(height)]
R = [[" " for i in range(height)] for j in range(height)]
W = [[" " for i in range(height)] for j in range(height)]
A = [[" " for i in range(height)] for j in range(height)]
N = [[" " for i in range(height)] for j in range(height)]

for row in range(height):
    for col in range(height):
        if col == 0 or col == height - 1 or (row == col and row < height // 2) or (row + col == height - 1 and row < height // 2):
            M[row][col] = "*"

for row in range(height):
    for col in range(height):
        if ((col == 0 or col == height-2) and row != 0) or ((row == 0 or row == height//2) and (col > 0 and col < height-2)):
            A[row][col] = "*"

for row in range(height):
    for col in range(height):
     if col == 0 or (row == 0 or row == height // 2) and (col > 0 and col < height - 1) or (col == height - 1 and row < height // 2) or (row == col and row > height // 2):
        R[row][col] = "*"

for row in range(height):
    for col in range(height):
        if col == 0 or col == height - 1 or (row == col and row >= height // 2) or (row + col == height - 1 and row >= height // 2):
            W[row][col] = "*"

for row in range(height):
    for col in range(height):
        if col == 0 or col == height - 1 or (row == col):
            N[row][col] = "*"


for i in range(height):
    for j in range(height):
        print(M[i][j], end="")
    print(end="  ")
    for j in range(height):
        print(A[i][j], end="")
    print(end="  ")
    for j in range(height):
        print(R[i][j], end="")
    print(end="  ")
    for j in range(height):
        print(W[i][j], end="")
    print(end="  ")
    for j in range(height):
        print(A[i][j], end="")
    print(end="  ")
    for j in range(height):
        print(N[i][j], end="")
    print(end="  ")
    print()