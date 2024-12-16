
width = 101
height = 103
seconds = 100

class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
    
    def move(self):
        for _ in range(seconds):
            new_x = ((self.position[0] + self.velocity[0]) + width)%width
            new_y = ((self.position[1] + self.velocity[1]) + height)%height
            self.position = (new_x,new_y)

grid_start = []
grid_finish = []

with open("example.txt") as f:
    lines = f.readlines()
    for line in lines:
        position = tuple(map(int, line.split(" ")[0].split("=")[1].split(",")))
        velocity = tuple(map(int, line.split(" ")[1].split("=")[1].split(",")))
        robot = Robot(position,velocity)
        # grid_start.append(robot.position)
        robot.move()
        grid_finish.append(robot.position)



def part_one():
    x_mid = width // 2  
    y_mid = height // 2  

    q1 = 0 
    q2 = 0
    q3 = 0 
    q4 = 0

    # Iterate through the coordinates
    for (x, y) in grid_finish:
        if x == x_mid or y == y_mid:
            continue  
        elif x > x_mid and y > y_mid:
            q1 += 1
        elif x < x_mid and y > y_mid:
            q2 += 1
        elif x < x_mid and y < y_mid:
            q3 += 1
        elif x > x_mid and y < y_mid:
            q4 += 1

    print(q1*q2*q3*q4)

part_one()