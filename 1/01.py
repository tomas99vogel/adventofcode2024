with open('input.txt') as f:
    lines = f.readlines()

first_row = [int(line.split("   ")[0]) for line in lines]
second_row = [int(line.split("   ")[1]) for line in lines]

def part_one():
    sorted_first = sorted(first_row)
    sorted_second = sorted(second_row)

    distances = 0
    for x,y in zip(sorted_first, sorted_second):
        distances += abs(x - y)

    return distances

def part_two():
    similarity_score = 0
    hashmap = {x:0 for x in first_row}

    for y in second_row:
        if y in hashmap.keys():
            hashmap[y] += 1

    for i in first_row:
        similarity_score += i * hashmap[i]

    return similarity_score

if __name__  == '__main__':
    print(part_one())
    print(part_two())
