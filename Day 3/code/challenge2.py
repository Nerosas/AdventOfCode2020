slopes = "../files/input.txt"
graph = []
with open(slopes) as s:
    for x in s:
        graph.append(x.strip())

def count_trees(right, down):
    count = 0
    x_coord = 0
    for y_coord in range(0, len(graph), down):
        try:
            point = graph[y_coord][x_coord]
        except IndexError:
            x_coord = x_coord % len(graph[y_coord])
            point = graph[y_coord][x_coord]
            
        if point == '#':
            count += 1
            
        x_coord += right

    return count

print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))
