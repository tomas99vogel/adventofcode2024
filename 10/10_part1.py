with open("input.txt") as f:
    grid = [[int(i) for i in line.strip()] for line in f]

heigth = len(grid)
width = len(grid[0])

directions = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1)
]

starting_points = []
for x in range(heigth):
    for y in range(width):
        if grid[x][y] == 0:
            starting_points.append((x,y))

def vector_sum(point,vector):
    next_point = (point[0] + vector[0], point[1] + vector[1])
    if next_point[0] in range(heigth) and next_point[1] in range(width):
        return next_point
    return None, None

def seek_path(point: tuple, i):
    if i == 10:
        trail_ends.add(point)
        return 1
    count = 0
    for dir in directions:
        nx, ny = vector_sum(point, dir)
        if nx is not None and grid[nx][ny] == i:
            count += seek_path((nx, ny), i + 1) 
    return count

part_one = 0
part_two = 0
for point in starting_points:
    trail_ends = set()
    part_two += seek_path(point, 1)
    part_one += len(trail_ends)

print(part_one)
print(part_two)
