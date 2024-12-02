# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

def check_report(line:list[int]) -> int:
    get_direction = line[0] - line[1]
    # >1 descending, <1 ascending
    if get_direction in range(-3,0): 
        for i in range(1,len(line)-1):
            if line[i]-line[i+1] not in range(-3,0):
                return 0
        return 1
    elif get_direction in range(1,4):
        for i in range(1,len(line)-1):
            if line[i]-line[i+1] not in range(1,4):
                return 0
        return 1
    else:
        return 0 # not safe

def part_one() -> int:
    safe_count = sum([check_report(line) for line in lines])
    return safe_count

if __name__ == '__main__':
    with open("input.txt") as f:
        lines = [list(map(int, line.split())) for line in f.readlines()]

    print(part_one())
    