numbers = "../files/input.txt"
with open(numbers) as n:
    numbers_list = [int(number.strip()) for number in n]


target = 31161678
target_list = []
count = 0
second_count = 0
while sum(target_list) != target:
    target_list = numbers_list[count:second_count]
    second_count += 1
    if sum(target_list) > target:
        count += 1
        second_count = count

print(min(target_list) + max(target_list))
