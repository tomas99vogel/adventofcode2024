
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

def seek_word(x:int, y:int, d, i):
    x = x + d[0]
    y = y + d[1]
    i += 1
    if i == len(word):
        return 1
    try:
        if lines[x][y] == word[i]:
            return seek_word(x, y, d, i)
        else:
            return 0
    except IndexError:
        return 0
    
if __name__ == '__main__':
    with open("example.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    count = 0
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            i = 0
            if lines[x][y] == word[i]:
                for d in directions:
                    if seek_word(x,y,d,i):
                        count += 1
    print(count)
            
        