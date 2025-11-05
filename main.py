# find raftel !!
# create empty map
# map_x = 0
# map_y = 0
import array as arr
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def mapSize(map_x, map_y):
    map_x, map_y = [int(i) for i in input("What size is your map [x,y]...").split(",")]
    return map_x, map_y


def inputIslands(a_coord_x, a_coord_y, b_coord_x, b_coord_y, c_coord_x, c_coord_y):
    # take user input for A,B,C island locations
    a_coord_x, a_coord_y = [
        int(i)
        for i in input("enter the coordinates of the first island [x,y]... ").split(",")
    ]
    b_coord_x, b_coord_y = [int(i) for i in input("second island... ").split(",")]
    c_coord_x, c_coord_y = [int(i) for i in input("and the third island? ").split(",")]
    print(
        "Checking, A=[",
        a_coord_x,
        ",",
        a_coord_y,
        "], B=[",
        b_coord_x,
        ",",
        b_coord_y,
        "], and C=[",
        c_coord_x,
        ",",
        c_coord_y,
        "]...",
    )
    confirm = input("Confirm [y/n]... ")
    if confirm == "y":
        print("Let's go")
    # this is a crazy return statement for all the island coordinates lmao
    return a_coord_x, a_coord_y, b_coord_x, b_coord_y, c_coord_x, c_coord_y


def setIslands(
    map_x,
    map_y,
    map_grid,
    a_coord_x,
    a_coord_y,
    b_coord_x,
    b_coord_y,
    c_coord_x,
    c_coord_y,
):
    # print(a_coord_x, a_coord_y)
    # print(map_grid[a_coord_x][a_coord_y])
    # for x in range(map_x):
    #     if x == a_coord_x:
    #         for y in range(map_y):
    #             if y == a_coord_y:
    #                 map_grid[x][y] = "A"
    #     elif x == b_coord_x:
    #         for y in range(map_y):
    #             if y == b_coord_y:
    #                 map_grid[x][y] = "B"
    #     elif x == c_coord_x:
    #         for y in range(map_y):
    #             if y == c_coord_y:
    #                 map_grid[x][y] = "C"
    # print(map_grid[a_coord_x][a_coord_y])

    print("in here")

    # trying to represent the spaces with the letters A, B, or C
    # a = "A"

    print("a:",a_coord_x,a_coord_y)
    print("b:",b_coord_x,b_coord_y)
    print("c:",c_coord_x,c_coord_y)
    # print("map_grid:",map_grid[a_coord_y][a_coord_x])

    # when i try to inset the A, it gets added to the whole column, all y++/-- values
    map_grid[a_coord_y][a_coord_x] = "A"
    print("map_grid[a_coord_y][a_coord_x]:",map_grid[a_coord_y][a_coord_x])
    print("map_grid[a_coord_y+1][a_coord_x]:",map_grid[a_coord_y+1][a_coord_x])


    # map_grid[b_coord_x][b_coord_y] = "B"
    # map_grid[c_coord_x][c_coord_y] = "C"

    # TEST
    print(map_grid[a_coord_x][a_coord_y])
    return map_grid


def prettyPrint(map_x, map_y, map_grid):
    # map has inverted y values, grid prints from 0 {top left}, down to y max {bottom left}
    for y in range(map_y):
        print('yo, y=',y)
        for x in range(map_x):
            # print('x=',x)
            print(map_grid[y][x], end="     ")
        print("\n")


def main():
    # start map empty
    a_coord_x, a_coord_y, b_coord_x, b_coord_y, c_coord_x, c_coord_y = 5, 3, 1, 3, 8, 6
    map_x, map_y = 10, 10

    # get map size and island location
    # map_x, map_y = mapSize(map_x, map_y)
    # a_coord_x, a_coord_y, b_coord_x, b_coord_y, c_coord_x, c_coord_y = inputIslands(
    #     a_coord_x, a_coord_y, b_coord_x, b_coord_y, c_coord_x, c_coord_y
    # )

    # create blank map grid
    # map_grid = [[0] * map_x] * map_y
    # map_grid = [map_x * [0]]* map_y

    xpoints = np.array([0, map_x])
    ypoints = np.array([0, map_y])

    plt.plot(xpoints, ypoints)
    plt.show()

    # # create map with islands
    # map_grid = setIslands(
    #     map_x,
    #     map_y,
    #     map_grid,
    #     a_coord_x,
    #     a_coord_y,
    #     b_coord_x,
    #     b_coord_y,
    #     c_coord_x,
    #     c_coord_y,
    # )

    # # final print
    # prettyPrint(map_x, map_y, map_grid)


main()
# prettyPrint(map_grid)
