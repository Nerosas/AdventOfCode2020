file = "../files/input.txt"
list_expenses = []
with open(file) as f:
    for line in f:
        list_expenses.append(int(line.strip()))

for i in range(len(list_expenses)):
    for j in range(i, len(list_expenses)):
        for k in range(j, len(list_expenses)):
            if list_expenses[i] + list_expenses[j] + list_expenses[k] == 2020:
                print(list_expenses[i] * list_expenses[j] * list_expenses[k])
