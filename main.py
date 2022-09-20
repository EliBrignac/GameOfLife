
import pprint
import time

grid = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,1,1,1,0,0,0],
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]

# any cell with 2 or 3 neighbors survives
def move_right(y, x):
    if x+1 == len(grid):
        return 0
    return (grid[y][x+1])

def move_left(y,x):
    if x-1 < 0:
        return 0
    return grid[y][x-1]

def move_up(y,x):
    if y-1 < 0:
        return 0
    return grid[y-1][x]

def move_down(y,x):
    if y+1 == len(grid):
        return 0
    return grid[y+1][x]

def move_north_east(y, x):
    if y-1 < 0 or x+1 == len(grid):
        return 0
    return grid[y-1][x+1]

def move_south_east(y,x):
    if y+1 == len(grid) or x+1 == len(grid):
        return 0
    return grid[y+1][x+1]

def move_north_west(y,x):
    if y-1 < 0 or x-1 < 0:
        return 0
    return grid[y-1][x-1]

def move_south_west(y,x):
    if y+1 == len(grid) or x-1 < 0:
        return 0
    return grid[y+1][x-1]


def check_neighboring_cells(y, x):
    # grid points are (y,x)
    sum = move_right(y,x) + move_left(y,x) + move_up(y,x) + move_down(y,x) + move_north_east(y,x) + move_south_east(y,x) + move_north_west(y,x) + move_south_west(y,x)
    #print(sum)
    return sum

def make_temp_grid():
    temp_grid = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,1,1,1,0,0,0],
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]
    return temp_grid

def set_grid(temp_grid):
    grid = temp_grid
    return grid

def play_game():
    temp_grid = make_temp_grid()
    for y in range(0,len(grid)):
        for x in range(0,len(grid[0])):
            #print(y,x)
            neighboring_cells = check_neighboring_cells(y,x)
            if neighboring_cells == 3 or neighboring_cells == 2:
                if neighboring_cells == 3:
                    temp_grid[y][x] = 1
                else:
                    temp_grid[y][x] = grid[y][x]
            else:
                temp_grid[y][x] = 0
    return temp_grid

for i in range(0,10):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(grid)
    print("\n")
    grid = play_game()
    time.sleep(1)




