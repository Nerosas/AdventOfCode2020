adapters = "../files/input.txt"
with open(adapters) as a:
    list_of_adapters = [int(j.strip()) for j in a]

current = 0
one_jolt_differences = 0
three_jolt_differences = 1

while list_of_adapters != []:
    candidate = min(list_of_adapters)
    difference = candidate - current
    if difference > 3:
        print("Failed.")
        break
    if difference == 3:
        three_jolt_differences += 1
    if difference == 1:
        one_jolt_differences += 1

    current = candidate

    list_of_adapters.pop(list_of_adapters.index(candidate))

print(one_jolt_differences * three_jolt_differences)
