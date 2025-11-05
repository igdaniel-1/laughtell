# find raftel !!
# create empty map
# map_x = 0
# map_y = 0
import array as arr
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

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

    print("in here")

    # trying to set the spaces with the letters A, B, or C


    # TEST
    # print(map_grid[a_coord_x][a_coord_y])
    return map_grid





def main():
    # start map empty
    a_coord_x, a_coord_y, b_coord_x, b_coord_y, c_coord_x, c_coord_y = 5, 3, 1, 3, 8, 6
    map_x, map_y = 10, 10

    # get map size and island location
    # map_x, map_y = mapSize(map_x, map_y)
    # a_coord_x, a_coord_y, b_coord_x, b_coord_y, c_coord_x, c_coord_y = inputIslands(
    #     a_coord_x, a_coord_y, b_coord_x, b_coord_y, c_coord_x, c_coord_y
    # )

    # xpoints = np.array([0, map_x])
    # ypoints = np.array([0, map_y])

    # plot points A, B, and C
    plt.plot(a_coord_x, a_coord_y, ".")
    plt.plot(b_coord_x, b_coord_y, ".")
    plt.plot(c_coord_x, c_coord_y, ".")
    # plt.plot(xpoints, ypoints)
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


main()
