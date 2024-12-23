
with open("example.txt") as f:
    grid = [line.strip() for line in f]

height = len(grid)
width = len(grid[0])

cache = {}

directions = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1)
]

def in_bounds(x, y):
    return 0 <= x < height and 0 <= y < width

def count_perimeter(letter, position):
    stack = [position]  
    visited.add(position) 
    perimeter = 0
    count = 1

    while stack:
        x, y = stack.pop()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not in_bounds(nx, ny) or grid[nx][ny] != letter:
                perimeter += 1
            elif (nx, ny) not in visited:
                count += 1
                visited.add((nx, ny))
                stack.append((nx, ny))

    return perimeter, count

visited = set() 
fields = {}
part_one = 0

for x in range(height):
    for y in range(width):
        if (x, y) not in visited:
            letter = grid[x][y]
            perimeter,count, sides = count_perimeter(letter, (x, y)) 

            fields[(letter, (x, y))] = (perimeter,count)
            part_one += perimeter*count

print(part_one)