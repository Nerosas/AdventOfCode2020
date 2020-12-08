microcode = "../files/input.txt"
instructions = []
with open(microcode) as m:
    for line in m:
        instructions.append(line.strip())
        
def run_code():
    accumulator = 0
    count = 0
    list_of_counts = []
    while count < len(instructions):
        if count not in list_of_counts:
            list_of_counts.append(count)
        else:
            return False, accumulator, list_of_counts

        instruction, operation, operand = process_instruction(instructions, count)
        if operation == 'acc':
            accumulator += operand
            count += 1
        if operation == 'jmp':
            count += operand
        if operation == 'nop':
            count += 1
    return True, accumulator, list_of_counts

def switch_operator(instruction):
    operator = instruction[0][0]
    if operator == 'jmp':
        instruction[0][0] = 'nop'
    elif operator == 'nop':
        instruction[0][0] = 'jmp'

    return instruction

def flip_instruction(instruction):
    instruction = switch_operator(instruction)
    instructions[instruction[1]] = instruction[0][0] + ' ' + instruction[0][1]

def process_instruction(instructions, count):
    instruction = instructions[count].split(' ')
    operation = instruction[0]
    operand = int(instruction[1])

    return instruction, operation, operand

def find_possible_faulty_instructions():
    outcome, accumulator, list_of_counts = run_code()
    faulty_instructions = []
    for count in list_of_counts:
        instruction, operation, operand = process_instruction(instructions, count)
        if operation == 'jmp' or operation == 'nop':
            faulty_instructions.append((instruction, count))

    return faulty_instructions
    

def change_code():
    faulty_instructions = find_possible_faulty_instructions()
    for instruction in faulty_instructions:
        flip_instruction(instruction)
        test_succeeded, accumulator, list_of_counts = run_code()
        if test_succeeded:
            return accumulator
        if not test_succeeded:
            flip_instruction(instruction)

print(change_code())
