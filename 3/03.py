import re

exp_part_one = r"mul\((\d{1,3},\d{1,3})\)"

exp_part_two = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"

with open("input.txt") as f:
    text = "".join(line for line in f.readlines())

def part_one(text):
    result = 0
    matches = re.findall(exp_part_one,text)
    for m in matches:
        digits = list(map(int,m.split(",")))
        result += int(digits[0])*int(digits[1])
    return result

def part_two(text):
    result = 0
    matches = re.findall(exp_part_two, text)
    valid = True
    for match in matches:
        if match == "don't()":
            valid = False
        elif match == "do()":
            valid = True
        elif valid:
            digits = re.findall("\d+", match)
            result += int(digits[0])*int(digits[1])
    return result

if __name__ == '__main__':
    print(part_one(text))
    print(part_two(text))
    