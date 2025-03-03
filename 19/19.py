from functools import cache

with open("input.txt") as f:
    towels = [towel.strip() for towel in f.readline().split(",")]
    patterns = [line.strip() for line in f.readlines() if line != "\n"]

@cache
def try_towels(pattern):
    if len(pattern) == 0:
        return 1
    for towel in towels:
        if pattern.startswith(towel):
            if try_towels(pattern[len(towel):]):
                return 1
    return 0

part_one = 0

for pattern in patterns:
    part_one += try_towels(pattern)
    
print(part_one)