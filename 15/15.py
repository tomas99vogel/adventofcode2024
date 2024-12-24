import os
import time

with open("input.txt") as f:
    grid = []
    line = f.readline().strip()
    while line != "":
        grid.append(list(line))
        line = f.readline().strip()
    instructions = "".join([line.strip() for line in f.readlines()])

height = len(grid)
width = len(grid[0])

directions = {
              ">": 1j,  
              "<": -1j, 
              "v": 1,  
              "^": -1 
            } 
def convert_complex_to_int(position):
    return int(position.real), int(position.imag)

# helper visualization
def print_grid(grid):
    os.system('clear')
    for row in grid:
        print("".join(map(str, row)))
    time.sleep(0.2)

def move_boxes(position, direction):
    next_position = position + direction
    nx, ny = convert_complex_to_int(next_position)
    stack = [(nx,ny)]
    while grid[nx][ny] == "O":
        next_position += direction
        nx, ny = convert_complex_to_int(next_position)
        stack.append((nx,ny))
    
    if grid[nx][ny] == "#":
        return position - direction
    if grid[nx][ny] == ".":
        while stack:
            nx,ny = stack.pop()
            grid[nx][ny] = "O"
        return position

def get_next_position(position,direction):
    next_position = position + direction
    x, y = convert_complex_to_int(next_position)

    if grid[x][y] == "#":
        return position
    elif grid[x][y] == "O":
        return move_boxes(next_position,direction)
    else:
        return next_position

# cached statring point, no reason in traversing the grid for it
position = 24 + 24j

for d in instructions:
    x, y = int(position.real), int(position.imag)
    position = get_next_position(position, directions[d])
    nx, ny = int(position.real), int(position.imag)
    if (x,y) == (nx,ny):
        pass
    else:
        grid[nx][ny] = "@"
        grid[x][y] = "."
    #print_grid(grid)

part_one = 0
for x in range(height):
    for y in range(width):
         if grid[x][y]=="O":
             part_one += 100*x+y
print(part_one)



