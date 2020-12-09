numbers = "../files/input.txt"
with open(numbers) as n:
    numbers_list = [int(number.strip()) for number in n]

start = 25
for number in range(start, len(numbers_list)):
    value = numbers_list[number]
    valid = False
    for i in range(number - 25, number):
        for j in range(i, number):
            if numbers_list[i] + numbers_list[j] == value:
                valid = True
                break
    if not valid:
        print(value)
        break
