dict_seat = {}
with open('xxx.csv',encoding='utf-8')as f:
    for row in f:
        columns = row.rstrip().split(',')
        name = columns[0]
        seat = columns[1]
        
        dict_seat[seat] = name

book_seat = sorted(dict_seat.items())

for seat, name in book_seat:
    print(seat,name)
