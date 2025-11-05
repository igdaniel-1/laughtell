# find raftel !!
# create empty map
# map_x = 0
# map_y = 0
import array as arr
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def setIslands(
    a_coord_x,
    a_coord_y,
    b_coord_x,
    b_coord_y,
    c_coord_x,
    c_coord_y,
):

    print("in here")

    # plot points A, B, and C
    plt.plot(a_coord_x, a_coord_y, ".")
    plt.plot(b_coord_x, b_coord_y, ".")
    plt.plot(c_coord_x, c_coord_y, ".")


    # TEST
    # print(map_grid[a_coord_x][a_coord_y])
    # return map_grid

def setPossibleDLocations(
    a_coord_x,
    a_coord_y,
    b_coord_x,
    b_coord_y,
    c_coord_x,
    c_coord_y,
):
    # for all grid locations
    # if grid location != island A|B|C --> possible D location


    # A to B, C to D CHECK
    # create a line from A to B
    # create another line from C to D
    # check if the lines make an X
    # if the C-->D line intersect A-->B line between XofA and XofB
        # possibleRaftelLocations += intersection point of CD and AB

    # A to C, B to D CHECK

    # A to D, B to C CHECK







def main():
    # get map size and island location
    map_x, map_y = 10, 10
    a_coord_x, a_coord_y, b_coord_x, b_coord_y, c_coord_x, c_coord_y = 5, 3, 1, 3, 8, 6
    

    # start map empty



    # map_x, map_y = mapSize(map_x, map_y)
    # a_coord_x, a_coord_y, b_coord_x, b_coord_y, c_coord_x, c_coord_y = inputIslands(
    #     a_coord_x, a_coord_y, b_coord_x, b_coord_y, c_coord_x, c_coord_y
    # )

    # xpoints = np.array([0, map_x])
    # ypoints = np.array([0, map_y])

    
    

    # create map with islands
    setIslands(
        a_coord_x,
        a_coord_y,
        b_coord_x,
        b_coord_y,
        c_coord_x,
        c_coord_y,
    )

    setPossibleDLocations(
        a_coord_x,
        a_coord_y,
        b_coord_x,
        b_coord_y,
        c_coord_x,
        c_coord_y,
    )

    # plt.plot(xpoints, ypoints)
    plt.show()


main()
