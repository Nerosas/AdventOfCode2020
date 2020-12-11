adapters = "../files/test1.txt"
with open(adapters) as a:
    list_of_adapters = [int(j.strip()) for j in a]

list_of_adapters = sorted(list_of_adapters)

start = 0

options = 1
while list_of_adapters != []:
    next_three = list_of_adapters[0:3]
    list_of_adapters = list_of_adapters[3:]
    #print(next_three)
    for candidate in next_three:
        difference = candidate - start
        #print(candidate, difference)
        if difference > 3:
            next_three.remove(candidate)

    if next_three != []:
        next_candidate = max(next_three)
        start = next_candidate
        next_three.remove(next_candidate)
        #print(next_three)
        if len(next_three) != 0:
            new_options = 2 * len(next_three)
        else:
            new_options = 1
        options *= new_options
        


print(options)
