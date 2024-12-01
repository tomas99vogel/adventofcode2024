with open('input.txt') as f:
    lines = f.readlines()

# parse input
first_list = [int(line.split()[0]) for line in lines]
second_list = [int(line.split()[1]) for line in lines]

def part_one() -> int:
    sorted_first = sorted(first_list)
    sorted_second = sorted(second_list)

    distances = sum(abs(x-y) for x,y in zip(sorted_first,sorted_second))

    return distances

def part_two() -> int:
    similarity_score = 0
    hashmap = {x:0 for x in first_list}

    for y in second_list:
        if y in hashmap.keys():
            hashmap[y] += 1

    for i in first_list:
        similarity_score += i * hashmap[i]

    return similarity_score

if __name__  == '__main__':
    print(part_one())
    print(part_two())
