from math import log10

with open("example.txt") as f:
    line = [int(i) for i in f.readline().strip().split()]

print(line)

cache = {}
def blink(i: int, blinks: int) -> int:
    if (i, blinks) in cache:
        return cache[(i, blinks)] 

    if blinks == 0:
        return 1
    if i == 0:
        result = blink(1, blinks - 1)
    else:
        num_len = int(log10(i)) + 1
        if num_len % 2 == 0:
            i1 = i % (10**(num_len//2))
            i2 = i // (10**(num_len//2))
            result = blink(i1, blinks - 1) + blink(i2, blinks - 1)
        else:
            result = blink(i * 2024, blinks - 1)

    cache[(i, blinks)] = result
    return result

part_one = 0
part_two = 0
for i in line:
    part_one += blink(i, 25)
    part_two += blink(i, 75)

print(part_one)
print(part_two)