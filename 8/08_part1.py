

with open("input.txt") as f:
    lines = [line.strip() for line in f]

antennas = {}

for x in range(len(lines)):
    for y in range(len(lines)):
        if lines[x][y] != ".":
            if lines[x][y] in antennas.keys():
                antennas[lines[x][y]].append((x,y))
            else:
                antennas[lines[x][y]] = [(x,y)]

def vector_dir(point1, point2):
    return (point1[0] - point2[0], point1[1] - point2[1])

def get_pairs(key):
    pairs = []
    for i in range(len(antennas[key])):
        for j in range(i+1,len(antennas[key])):
            pairs.append((antennas[key][i], antennas[key][j]))
    return pairs

def in_range(node):
    return node[0] in range(len(lines)) and node[1] in range(len(lines))

antinodes = set()
def get_antinodes():
    for key in antennas.keys():
        pairs = get_pairs(key)
        for pair in pairs:
            vector = vector_dir(pair[0], pair[1])

            antinode1 = (pair[0][0]+vector[0], pair[0][1]+vector[1])
            antinode2 = (pair[1][0]-vector[0], pair[1][1]-vector[1])
            
            if in_range(antinode1) and antinode1 not in pair:
                antinodes.add(antinode1)

            if in_range(antinode2) and antinode2 not in pair:
                antinodes.add(antinode2)
                
get_antinodes()
print(len(set(antinodes)))
