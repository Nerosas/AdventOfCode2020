import re
rules = "../files/test.txt"
rules_list = []
with open(rules) as r:
    rules_list = [rule.strip() for rule in r]


class BagTree:
    searched_colours = []
    def __init__(self, colour, number):
        self.colour = colour
        self.children = []
        self.number = number
        self.count = number
        
    def add_children(self):
        search = []
        for rule in rules_list:
            if self.colour not in BagTree.searched_colours:
                search = re.findall(self.colour + " bags contain", rule)
            if search != []:
                try:
                    found = rule.split(self.colour)[1]
                    if found == " no other bags.":
                        break
                    found = found.split("bags contain")
                    found = found[1].split("bag")
                    #print(self.colour + " bags contain")
                    for c in range(len(found)):
                        found[c] = found[c].strip('s').strip(',').strip(' ').split(' ')
                        try:
                            number = int(found[c][0])
                        except ValueError:
                            continue
                        colour = found[c][1] + ' ' + found[c][2]
                        #print(number, colour)
                        self.children.append(BagTree(colour, number))
                except IndexError:
                    continue
                BagTree.searched_colours.append(self.colour)
        for c in self.children:
            c.add_children()

    def count_children(self):
        if self.children == []:
            return self.number
        for child in self.children:
            self.count += child.count_children()
        return self.count * self.number

shiny_gold = BagTree("shiny gold", 1)
shiny_gold.add_children()
print(shiny_gold.count_children() - 1)
