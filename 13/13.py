import re

is_part_two = True

def solve_linear_equations(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return 0  
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    if x.is_integer() and y.is_integer():
        return int(x), int(y)
    else:
        return 0,0

with open("input.txt") as f:
    lines = f.readlines()

prizes = []
tmp = []
for line in lines:
    if line == "\n":
        prizes.append(tmp)
        tmp = []
    else:
        tmp.extend(list(map(int, re.findall(r"\d+", line.strip()))))

for idx,prize in enumerate(prizes):
    prizes[idx][1], prizes[idx][2] = prizes[idx][2],prizes[idx][1]
    prizes[idx][2], prizes[idx][4] = prizes[idx][4],prizes[idx][2]
    prizes[idx][3], prizes[idx][4] = prizes[idx][4],prizes[idx][3]
    if is_part_two:
        prizes[idx][2] += 10000000000000
        prizes[idx][5] += 10000000000000      

total = 0
for nums in prizes:
    x,y = solve_linear_equations(*nums)
    if (x > 0 and y > 0):
        print((x,y))
        total += 3*x + y
print(total)

