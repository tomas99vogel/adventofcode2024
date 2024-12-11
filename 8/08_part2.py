with open("input.txt") as f:
    lines = [line.strip() for line in f]

limit = len(lines)

antennas = {}
for x in range(len(lines)):
    for y in range(len(lines[x])):
        if lines[x][y] != ".":
            if lines[x][y] in antennas.keys():
                antennas[lines[x][y]].append((x,y))
            else:
                antennas[lines[x][y]] = [(x,y)]

def vector_dir(point1, point2):
    return ((point1[0] - point2[0], point1[1] - point2[1]), (point2[0] - point1[0], point2[1] - point1[1]))

def get_pairs(key):
    pairs = []
    for i in range(len(antennas[key])):
        for j in range(i+1,len(antennas[key])):
            pairs.append((antennas[key][i], antennas[key][j]))
    return pairs

def in_range(node):
    return node[0] in range(limit) and node[1] in range(limit)

antinodes_part_2 = set()

def get_antinodes():
    for key in antennas.keys():
        pairs = get_pairs(key)
        for pair in pairs:
            vectors = vector_dir(pair[0], pair[1])
            for vector in vectors:
                next_node = (pair[0][0], pair[0][1])
                
                while in_range(next_node):
                    antinodes_part_2.add(next_node)  
                    next_node = (next_node[0] - vector[0], next_node[1] - vector[1])      
                
get_antinodes()
print(len(antinodes_part_2))