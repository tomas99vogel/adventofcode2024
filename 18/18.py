from collections import deque

DIRECTIONS = [(0, 1),(0, -1), (-1, 0), (1, 0)] 
BYTES = 1024

start = (0, 0)  
end = (70, 70) 

falling_bytes = []
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        falling_bytes.append(tuple(map(int,line.strip().split(","))))

# create the grid and fill with falling bytes
grid = [["." for _ in range(71)] for _ in range(71)]
for i in range(BYTES):
    y,x = falling_bytes[i]
    grid[x][y] = "#"

# for line in grid:
#     print("".join(line))

def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])

    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = 0

    queue = deque()  
    # (cost, x, y, last_direction)
    queue.append((0, start[0], start[1]))

    while queue:
        cost, x, y = queue.popleft() 
        
        for (dx, dy) in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "#":

                new_cost = cost + 1

                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    print(nx,ny, dist[nx][ny])
                    queue.append((new_cost, nx, ny))

    return dist[end[0]][end[1]]



part_one = shortest_path(grid, start, end)
print(part_one)