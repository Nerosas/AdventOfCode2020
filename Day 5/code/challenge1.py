seats = "../files/input.txt"
seat_list = []
with open(seats) as s:
    for seat in s:
        seat_list.append(seat.strip())

def fetch_row(boarding_pass):
    row_list = [i for i in range(128)]
    for i in range(7):
        half = len(row_list)//2
        if boarding_pass[i] == 'F':
            row_list = row_list[:half]
        if boarding_pass[i] == 'B':
            row_list = row_list[half:]
    return row_list[0]

def fetch_col(boarding_pass):
    col_list = [i for i in range(8)]
    for i in range(7, 10):
        half = len(col_list)//2
        if boarding_pass[i] == 'L':
            col_list = col_list[:half]
        if boarding_pass[i] == 'R':
            col_list = col_list[half:]
    return col_list[0]

def max_seat_id():
    list_seat_id = []
    for i in seat_list:
        seat_id = fetch_row(i) * 8 + fetch_col(i)
        list_seat_id.append(seat_id)

    print(list_seat_id)
    return max(list_seat_id)

print(max_seat_id())
