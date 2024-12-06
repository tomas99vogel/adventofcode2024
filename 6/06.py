

with open("input.txt") as f:
    lines = [line.strip() for line in f]

def get_start() -> int:
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if lines[x][y] == "^":
                return x,y
    return None

x,y = get_start()

def gen_directions(directions):
    while 1:
        for d in directions:
            yield d

directions = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
]
rotation = gen_directions(directions)

visited = set([(x,y)])

# first step
next_x, next_y = next(rotation)
x = x + next_x
y = y + next_y
visited.add((x,y))
# continue until reaching an edge
while x+next_x in range(len(lines)) and y+next_y in range(len(lines)):
    if lines[x+next_x][y+next_y] in (".^"):
        x = x + next_x
        y = y + next_y
        visited.add((x,y))
    else:
        next_x, next_y = next(rotation)
print(visited, len(visited))
    


