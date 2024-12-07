def parse_line(line):
    tmp = line.split(":")
    target = int(tmp[0])
    nums = list(map(int, tmp[1].split()))
    return target, nums

def test_operations(target, num, i) -> bool:
    if i < len(nums):
        next = [num + nums[i], num * nums[i]]
        for n in next:
            if n == target:
                print(f"Found: {n} = {target}, {i}")
                return True
            if n > target:
                continue
            if test_operations(target,  n, i+1):
                return True
    return False


with open("input.txt") as f:
    lines = [line.strip() for line in f]

    part_one = 0
    for line in lines:
        target, nums = parse_line(line)
        for i in range(len(nums)-1):
            if test_operations(target, nums[i], i+1):
                part_one += target
                break
            

    print(part_one)

