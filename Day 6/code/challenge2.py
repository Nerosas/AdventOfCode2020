answers = "../files/input.txt"
answers_list = []
with open(answers) as a:
    for line in a:
        answers_list.append(line.strip())


def remove_duplicates(answers_list):
    for i in range(len(answers_list)):
        answers_list[i] = "".join(set(answers_list[i]))
    return answers_list


def group_answers(answers_list):
    count = 0
    item = 0
    count_list = []
    while item < len(answers_list):
        next_item = item + 1
        try:
            if answers_list[next_item] != '':
                answers_list[item] += answers_list[next_item]
                del answers_list[next_item]
                item -= 1
                count += 1
            else:
                count_list.append(count)
                count = 0
        except IndexError:
            count_list.append(count)
            return answers_list, count_list
        item += 1
    return answers_list, count_list

def count_answers(answers_list, count_list):
    answer_count = []
    for answer in range(len(answers_list)):
        questions_everyone_answered = []
        answers = []
        for char in answers_list[answer]:
            if answers_list[answer].count(char) == count_list[answer] and char not in answers:
                questions_everyone_answered.append(True)
            else:
                questions_everyone_answered.append(False)
            answers.append(char)
            
        answer_count.append(questions_everyone_answered.count(True))
    return answer_count

data = group_answers(remove_duplicates(answers_list))

print(sum(count_answers(data[0], data[1])))
