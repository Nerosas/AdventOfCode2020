passports = "../files/input.txt"
data = []
with open(passports) as p:
    for i in p:
        data.append(i.strip().split())


def clean_data():
    count = 0
    item = 0
    while count < len(data) - 1:
        next_item = item + 1
        try:
            if data[next_item] != []:
                data[item] += data[next_item]
                del data[next_item]
                item -= 1
        except IndexError:
            return data
        item += 1
    return data

def convert_to_dictionary(data):
    passport_dictionaries = []
    for passport in data:
        data_dict = {}
        for line in passport:
            entry = line.split(':')
            data_dict[entry[0]] = entry[1]
        passport_dictionaries.append(data_dict)

    return passport_dictionaries

def count_valid_passports(passport_dictionaries):
    count = 0
    for passport in passport_dictionaries:
        if len(passport) == 8:
            count += 1
        if len(passport) == 7:
            if 'cid' not in passport:
                count += 1
    return count

print(count_valid_passports(convert_to_dictionary(clean_data())))
