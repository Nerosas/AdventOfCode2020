import re

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

def valid_byr(byr):
    return 1920 <= int(byr) <= 2002

def valid_iyr(iyr):
    return 2010 <= int(iyr) <= 2020

def valid_eyr(eyr):
    return 2020 <= int(eyr) <= 2030

def valid_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_hgt(hgt):
    number = int(re.findall("[0-9]+", hgt)[0])
    unit = re.split("[0-9]+", hgt)[1]
    if unit == 'cm':
        if 150 <= number <=193:
            return True
    if unit == 'in':
        if 59 <= number <= 76:
            return True
    return False

def valid_hcl(hcl):
    if re.search("#([0-9]|[abcdef]){6}", hcl) is not None:
        return True
    return False

def valid_pid(pid):
    if len(pid) == 9:
        return True
    return False

def valid_passport(passport):
    list_of_checks = []
    try:
        list_of_checks.append(valid_pid(passport["pid"]))
        list_of_checks.append(valid_hcl(passport["hcl"]))
        list_of_checks.append(valid_hgt(passport["hgt"]))
        list_of_checks.append(valid_ecl(passport["ecl"]))
        list_of_checks.append(valid_eyr(passport["eyr"]))
        list_of_checks.append(valid_iyr(passport["iyr"]))
        list_of_checks.append(valid_byr(passport["byr"]))
    except KeyError:
        return False
    if False not in list_of_checks:
        return True
    return False

def count_valid_passports(passport_dictionaries):
    count = 0
    for passport in passport_dictionaries:
        if valid_passport(passport):
            count += 1
    return count

print(count_valid_passports(convert_to_dictionary(clean_data())))
