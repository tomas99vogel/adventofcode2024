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


def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])

    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = 0

    queue = deque()  
    # (cost, x, y)
    queue.append((0, start[0], start[1]))

    while queue:
        cost, x, y = queue.popleft() 
        
        for (dx, dy) in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "#":

                new_cost = cost + 1

                if new_cost < dist[nx][ny]:
                    
                    dist[nx][ny] = new_cost
                    if (nx, ny) == end:
                        # for line in dist:
                        #     print("".join(str(line)))
                        # print("\n")
                        return None
    return falling_bytes[i]

blocked_path = shortest_path(grid, start, end)
for i in range(BYTES, len(falling_bytes)):
    y,x = falling_bytes[i]
    grid[x][y] = "#"
    if not blocked_path:
        blocked_path = shortest_path(grid, start, end)
    else:
        print(blocked_path)
        break
