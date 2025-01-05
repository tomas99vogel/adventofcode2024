from functools import cache

with open("input.txt") as f:
    towels = [towel.strip() for towel in f.readline().split(",")]
    patterns = [line.strip() for line in f.readlines() if line != "\n"]

print(towels)
print(patterns)

count_possible_patterns = 0
 
@cache
def try_towels(pattern):
    if len(pattern) == 0:
        return 1
    possible_towels = [towel for towel in towels if pattern.startswith(towel)]
    for towel in possible_towels:
        if try_towels(pattern[len(towel):]):
            return 1
    for towel in possible_towels:
        return try_towels(pattern[len(towel)::])
    if not possible_towels:
        return 0

for pattern in patterns:
    count_possible_patterns += try_towels(pattern)
    
print(count_possible_patterns)