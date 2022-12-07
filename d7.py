rows = int(input("hello"))
col = rows + rows - 5
center = col // 2
for i in range(rows):
    for j in range(col):
        if i == 2 or i == (rows - 3) or i + j == center or j - i == center or i - j == 2 or i + j == col + 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()