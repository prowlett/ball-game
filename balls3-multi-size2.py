# fills the board 100k times each with 1-b^2 balls
# for boards from 2x2 to 8x8
# and plots the results on regular and y-log scales.
# N.B. ignoring the empty centre space

import matplotlib.pyplot as plt
from random import shuffle

runs = 10**6

boards_tried = []

for b in range(2,10):
    boards_tried.append(f"{b*b} board")

    num_balls_set = []
    successes_set = []

    for num_balls in range(1,b*b+1):
        balls = []
        while len(balls) < b*b:
            for i in range(0,num_balls):
                balls.append(i)
                if len(balls) == b*b: break

        # print(balls)        

        matches = 0
        for c in range(runs):
            # print(f"{num_balls} colours")
            shuffle(balls)
            theboard = []
            for i in range(b):
                thisrow = []
                for j in range(b):
                    thisrow.append(balls[i*b+j])
                theboard.append(thisrow)
            # # print board
            # for row in theboard:
            #     for col in row:
            #         print(col,end="")
            #     print()

            outputpieces = []
            match = False
            for i in range(b):
                for j in range(b):
                    if i-1 >= 0 and theboard[i][j] == theboard[i-1][j]:
                        # print(f"{i},{j} match row above")
                        match = True
                    if j-1 >= 0 and theboard[i][j] == theboard[i][j-1]:
                        # print(f"{i},{j} match column left")
                        match = True
                    if j+1 < b and theboard[i][j] == theboard[i][j+1]:
                        # print(f"{i},{j} match column right")
                        match = True
                    if i+1 < b and theboard[i][j] == theboard[i+1][j]:
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

    print(num_balls_set)
    print(successes_set)

    plt.plot(num_balls_set,successes_set)
    
    f = open(f"multicolours-1m-runs-{b}x{b}.csv","w+")
    f.write("Colours, Runs with match, Runs with no match\n")
    for row in range(len(num_balls_set)):
        f.write(f"{num_balls_set[row]},{runs-successes_set[row]},{successes_set[row]}\n")
    f.close()

    plt.legend(boards_tried)
    plt.xlabel("No. colours")
    plt.ylabel("No. times out of 1m with an adjacent pair")
    plt.yscale('log')
    plt.savefig(f"multicolours-1m-runs-log-plot-up-to-{b}x{b}.png")