answers = "../files/input.txt"
answers_list = []
with open(answers) as a:
    for line in a:
        answers_list.append(line.strip())

def group_answers():
    count = 0
    item = 0
    while count < len(answers_list) - 1:
        next_item = item + 1
        try:
            if answers_list[next_item] != '':
                answers_list[item] += answers_list[next_item]
                del answers_list[next_item]
                item -= 1
        except IndexError:
            return answers_list
        item += 1
    return answers_list

def remove_duplicates(answers_list):
    for i in range(len(answers_list)):
        answers_list[i] = "".join(set(answers_list[i]))
    return answers_list

def count_answers(answers_list):
    count = 0
    for answer in answers_list:
        count += len(answer)
    return count

print(count_answers(remove_duplicates(group_answers())))
