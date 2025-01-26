# fills the board a million times each with 1-80 balls
# and plots the results on regular and y-log scales.

import matplotlib.pyplot as plt
from random import shuffle

runs = 10**6

num_balls_set = []
successes_set = []

for num_balls in range(1,81):
    balls = []
    while len(balls) < 80:
        for i in range(0,num_balls):
            balls.append(i)
            if len(balls) == 80: break

    # print(balls)        

    matches = 0
    for c in range(runs):
        shuffle(balls)
        board = []
        for i in range(40):
            board.append(balls[i])
        board.append(-1) # blank space at centre
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
        # if not match:
        #     print(f"no match {c}")

    # print(f"{num_balls} balls:")
    # print(f"{matches}/{runs} there was a match")
    # print(f"{runs-matches}/{runs} there was no match")
    print(f"{num_balls}\t{matches}\t{runs-matches}")
    num_balls_set.append(num_balls)
    successes_set.append(runs-matches)

plt.plot(num_balls_set,successes_set)
plt.savefig("multiball-1m-runs-regular-plot.png")
plt.plot(num_balls_set,successes_set)
plt.yscale('log')
plt.savefig("multiball-1m-runs-log-plot.png")