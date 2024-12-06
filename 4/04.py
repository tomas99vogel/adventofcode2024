
word = "XMAS"

directions = [
    (0,1), # right
    (0,-1), # left
    (-1,1), # up-right
    (-1,-1), # up-left
    (-1,0), # up
    (1,1), # down-right
    (1,-1), # down-left
    (1,0) # down
]

part_two_directions = [
    (-1,1), # up-right
    (-1,-1), # up-left
    (1,1), # down-right
    (1,-1), # down-left
]

def seek_word(x:int, y:int, d, i):
    i += 1
    if i == len(word):
        return True
    if x not in range(len(lines)) or y not in range(len(lines)):
        return False
    if lines[x][y] == word[i]:
        return seek_word(x + d[0], y + d[1], d, i)
    else:
        return False

def part_one(lines):
    count = 0
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            i = 0
            if lines[x][y] == word[i]:
                for d in directions:
                    if seek_word(x + d[0], y + d[1], d, i):
                        count += 1
    return count

def part_two(lines):
    count = 0
    valid_strings = ["MMSS","MSMS","SSMM","SMSM"]
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if lines[x][y] == "A":
                string = ""
                for d in part_two_directions:
                    if x + d[0] not in range(len(lines)) or y + d[1] not in range(len(lines)):
                        break
                    if lines[x + d[0]][y + d[1]] in ("M", "S"):
                        string += (lines[x + d[0]][y + d[1]])
                    else:
                        break
                if string in valid_strings:
                    count += 1
    return count

                    
    
if __name__ == '__main__':
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    
    part_one_count = part_one(lines)
    part_two_count = part_two(lines)
    print(part_one_count)
    print(part_two_count)