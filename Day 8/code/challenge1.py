microcode = "../files/input.txt"
instructions = []
with open(microcode) as m:
    for line in m:
        instructions.append(line.strip())

accumulator = 0
count = 0
list_of_counts = []
while count < len(instructions):
    if count not in list_of_counts:
        list_of_counts.append(count)
    else:
        print(accumulator)
        break
    instruction = instructions[count].split(' ')
    operation = instruction[0]
    operand = int(instruction[1])

    if operation == 'acc':
        accumulator += operand
        count += 1
    if operation == 'jmp':
        count += operand
    if operation == 'nop':
        count += 1

