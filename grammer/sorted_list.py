employees = []

with open('xxx.csv',encoding='utf-8')as f:
    for row in f:
        columns = row.rstrip().split(',')
        number = columns[0]
        name = columns[1]
        joined_data = number + '_' + name
        employees.append(joined_data)

employees = sorted(employees)

for result in employees:
    print(result)
