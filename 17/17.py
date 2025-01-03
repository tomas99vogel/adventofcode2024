
instructions = [2,4,1,1,7,5,4,6,0,3,1,4,5,5,3,0]

a = 28066687
b = 0
c = 0

out = []

def get_operand(i:int):
    if i < 4:
        return i
    if i == 4:
        return a
    if i == 5:
        return b
    if i == 6:
        return c

ptr = 0

while ptr < len(instructions):
    op_code = instructions[ptr]
    operand = get_operand(instructions[ptr+1])
    
    match op_code:
        case 0:
            a = int(a//(2**operand))
        case 1:
            b = b ^ instructions[ptr+1]
        case 2:
            b = operand % 8 
        case 3:
            if a != 0:
                ptr = instructions[ptr+1]
                print(a)
                continue
        case 4:
            b = b ^ c
        case 5:
            out.append(operand % 8)
        case 6:
            b = int(a//(2**operand))
        case 7:
            c = int(a//(2**operand))
    ptr += 2

print(",".join(map(str,out)))


