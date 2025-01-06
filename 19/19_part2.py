from functools import cache

with open("input.txt") as f:
    towels = [towel.strip() for towel in f.readline().split(",")]
    patterns = [line.strip() for line in f.readlines() if line != "\n"]

@cache
def try_towels(pattern):
    if len(pattern) == 0:
        return 1
    possible_combinations = 0
    for towel in towels:
        if pattern.startswith(towel):
            possible_combinations += try_towels(pattern[len(towel):])
    return possible_combinations

count = 0
for pattern in patterns:
    count += try_towels(pattern)
print(count)
    