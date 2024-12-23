
width = 101
height = 103
seconds = 100
robots = []
grid = [["." for _ in range(height)] for _ in range(width)]

class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
    
    def move(self):
        try:
            grid[self.position[0]][self.position[1]] = "."
        except:
            pass
        new_x = ((self.position[0] + self.velocity[0]) + width)%width
        new_y = ((self.position[1] + self.velocity[1]) + height)%height
        self.position = (new_x,new_y)


with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        position = tuple(map(int, line.split(" ")[0].split("=")[1].split(",")))
        velocity = tuple(map(int, line.split(" ")[1].split("=")[1].split(",")))
        robot = Robot(position,velocity)
        robots.append(robot)

def print_grid(grid, steps):
    for row in grid:
        print("".join(map(str, row)))
    input(f"Press any key to continue... {steps}")

steps = 0
while True:
    lines_with_10_robots = 0
    for robot in robots:
        robot.move()
        grid[robot.position[0]][robot.position[1]] = "#"
    for row in grid:
        count_robots_in_line = 0
        for idx,c in enumerate(row):
            if row[idx] == '#':
                count_robots_in_line = 0
                i = idx
                while i < width and row[i+1] == '#':
                    count_robots_in_line += 1
                    i += 1
                if count_robots_in_line > 10:
                    lines_with_10_robots += 1
    steps += 1
    if lines_with_10_robots > 2:
        print_grid(grid, steps)
    



