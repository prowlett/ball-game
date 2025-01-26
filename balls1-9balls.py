# 0: red (20)
# 1: green (15)
# 2: yellow (15)
# 3: blue (10)
# 4: orange (10)
# 5: purple (10)

from random import shuffle

balls = []
for i in range(10):
    balls.append(0)
    balls.append(1)
    balls.append(2)
    balls.append(3)
    balls.append(4)
    balls.append(5)
for i in range(5):
    balls.append(0)
    balls.append(1)
    balls.append(2)
for i in range(5):
    balls.append(0)

matches = 0
runs = 10**6
for c in range(runs):
    shuffle(balls)
    board = []
    for i in range(40):
        board.append(balls[i])
    board.append(-1)
    for i in range(40):
        board.append(balls[i+40])
    theboard = []
    for i in range(9):
        thisrow = []
        for j in range(9):
            thisrow.append(board[i*9+j])
        theboard.append(thisrow)
    # # print board
    # for row in theboard:
    #     for col in row:
    #         print(col,end="")
    #     print()

    outputpieces = []
    match = False
    for i in range(9):
        for j in range(9):
            if i-1 >= 0 and theboard[i][j] == theboard[i-1][j]:
                # print(f"{i},{j} match row above")
                match = True
            if j-1 >= 0 and theboard[i][j] == theboard[i][j-1]:
                # print(f"{i},{j} match column left")
                match = True
            if j+1 < 9 and theboard[i][j] == theboard[i][j+1]:
                # print(f"{i},{j} match column right")
                match = True
            if i+1 < 9 and theboard[i][j] == theboard[i+1][j]:
                # print(f"{i},{j} match row below")
                match = True
        if match:
            matches += 1
            # print(f"match {c}")
            break
    if not match:
        print(f"no match {c}")

    print(f"{matches}/{runs} there was a match")
    print(f"{runs-matches}/{runs} there was no match")