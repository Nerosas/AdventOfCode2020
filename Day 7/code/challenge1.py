import re

rules = "../files/input.txt"
rules_list = []
with open(rules) as r:
    for rule in r:
        rules_list.append(rule.strip())

colours = ["shiny gold"]
for colour in colours:
    for rule in rules_list:
        search = re.findall(colour, rule)
        if search != []:
            rule = rule.split(" ")
            new_colour = rule[0] + " " + rule[1]
            if new_colour not in colours:
                colours.append(new_colour)

print(len(colours) - 1)
