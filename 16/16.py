from collections import deque
DIRECTIONS = [(0, 1),(0, -1), (-1, 0), (1, 0)] # starting east=right

def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])

    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = 0

    queue = deque()  
    # (cost, x, y, last_direction)
    queue.append((0, start[0], start[1], 0))

    while queue:
        cost, x, y, last_direction = queue.popleft() 
        
        for direction_index, (dx, dy) in enumerate(DIRECTIONS):
            nx, ny = x + dx, y + dy
            if grid[nx][ny] != "#":

                new_cost = cost + 1
                if direction_index != last_direction and last_direction != -1:
                    new_cost += 1000

                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    print(nx,ny, dist[nx][ny])
                    queue.append((new_cost, nx, ny, direction_index))

    return dist[end[0]][end[1]]

with open("input") as f:
    grid = [line.strip() for line in f]

start = (139, 1)  
end = (1, 139) 

part_one = shortest_path(grid, start, end)
print(part_one)