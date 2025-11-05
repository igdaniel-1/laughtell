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



# def prettyPrint(map_x, map_y, map_grid):
#     # map has inverted y values, grid prints from 0 {top left}, down to y max {bottom left}
#     for y in range(map_y):
#         print('yo, y=',y)
#         for x in range(map_x):
#             # print('x=',x)
#             print(map_grid[y][x], end="     ")
#         print("\n")