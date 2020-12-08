import re
rules = "../files/input.txt"
rules_list = []
with open(rules) as r:
    for rule in r:
        rules_list.append(rule.strip())

colours = ["shiny gold bags contain"]
count = [1]
counting = 0
advance = 0
for colour in colours:
    for rule in rules_list:
        search = re.findall(colour, rule)
        if search != []:
            try:
                found = rule.split(colour)[1]
                if found == " no other bags.":
                    advance = 0
                    continue
            except IndexError:
                continue
            
            if ',' in found:
                found = found.split(",")
                #counting += 1
                for b in range(len(found)):
                    advance = len(found) - 1
                    found[b] = found[b].strip(' ')
                    found[b] = found[b].split(' ')
                    count.append(count[counting] * int(found[b][0]))
                    print(count[counting], found[b], count)
                    new_exp = found[b][1] + ' ' + found[b][2] + " bags contain"
                    colour_already_searched = False
                    try:
                        colours.index(new_exp)
                    except ValueError:
                        colours.append(new_exp)
                counting += advance
print(sum(count))
