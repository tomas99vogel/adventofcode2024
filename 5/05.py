from functools import cmp_to_key

if __name__ == '__main__':
    with open("input.txt") as f:
        parts = f.read().split("\n\n")
        rules = [tuple(
                    map(int,(i for i in part.split("|")))) 
                    for part in parts[0].split()]
        pages = [list(
                    map(int,part.split(",")))
                    for part in parts[1].split()]

    rules_dict = {}
    for i in rules:
        if rules_dict.get(i[0]):
            rules_dict[i[0]].append(i[1])
        else:
            rules_dict[i[0]] = [i[1]]

    part_one = 0
    part_two = 0

    for line in pages:
        correct_line = True
        for idx, num in enumerate(line):
            if num in rules_dict.keys():
                for n in rules_dict[num]:
                    if n in line[:idx]:
                        correct_line = False
                        break
        
        if correct_line:
            part_one += line[int(len(line)/2)]
        else:
            cmp = cmp_to_key(lambda x,y: 1-2*((x,y) in rules))
            fixed_line = sorted(line, key=cmp)
            print(fixed_line)
            part_two += fixed_line[int(len(fixed_line)/2)]

    print(part_one)
    print(part_two)
                


