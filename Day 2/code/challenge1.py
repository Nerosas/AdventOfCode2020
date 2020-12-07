password_file = "../files/input.txt"
password_list = []
with open(password_file) as p:
    for password in p:
        password_list.append(password.strip())

count = 0
for password in password_list:
    split_password = password.split()
    numbers = split_password[0].split('-')
    letters = split_password[1].strip(':')
    password = split_password[2]
    min_number = int(numbers[0])
    max_number = int(numbers[1])
    
    instances = password.count(letters)
    
    if min_number <= instances <= max_number:
        count += 1

print(count)
