
def part_one_check(line:list[int]) -> int:
    get_diff = line[0] - line[1]
    if get_diff == 0 or get_diff < -3 or get_diff > 3:
        return 0
    if get_diff in range(-3,0): 
        for i in range(1,len(line)-1):
            if line[i]-line[i+1] not in range(-3,0):
                return 0
        return 1
    if get_diff in range(1,4):
        for i in range(1,len(line)-1):
            if line[i]-line[i+1] not in range(1,4):
                return 0
        return 1

def part_two_check(line:list[int]) -> int:
    if part_one_check(line):
        return 1
    else:
        for i in range(len(line)):
            if part_one_check(line[:i]+line[i+1::]):
                return 1
    return 0

if __name__ == '__main__':
    with open("input.txt") as f:
        lines = [list(map(int, line.split())) for line in f.readlines()]

    part_one = 0
    part_two = 0

    for line in lines:
        part_one += part_one_check(line)
        part_two += part_two_check(line)

    print(part_one)
    print(part_two)

  
    