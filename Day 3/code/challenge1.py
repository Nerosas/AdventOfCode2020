slopes = "../files/input.txt"
x_axis = []
with open(slopes) as s:
    for x in s:
        x_axis.append(x.strip())

count = 0
x_coord = 0
for y_coord in x_axis:
    try:
        point = y_coord[x_coord]
    except IndexError:
        x_coord = x_coord % len(y_coord)
        point = y_coord[x_coord]
        
    if point == '#':
        count += 1
        
    x_coord += 3

print(count)
