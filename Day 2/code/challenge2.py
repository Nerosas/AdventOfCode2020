password_file = "../files/input.txt"
password_list = []
with open(password_file) as p:
    for password in p:
        password_list.append(password.strip())

count = 0
for password in password_list:
    split_password = password.split()
    numbers = split_password[0].split('-')
    letter = split_password[1].strip(':')
    password = split_password[2]
    position_one = int(numbers[0]) - 1
    position_two = int(numbers[1]) - 1
    
    letter_one = password[position_one]
    letter_two = password[position_two]

    instances = letter_one.count(letter) + letter_two.count(letter)

    if instances == 1:
        count += 1

print(count)
