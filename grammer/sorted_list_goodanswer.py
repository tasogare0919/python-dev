employees = []
# データの取得
with open('input/employees.csv', encoding='utf-8') as f:
    for row in f:
        columns = row.strip().split(',')
        employee_id = columns[0]
        employee_name = columns[1]
        employee = '{employee_id}_{employee_name}'.format(employee_id=employee_id,
                                                          employee_name=employee_name)
        employees.append(employee)
# 並び替え
sorted_employees = sorted(employees)

# 表示
for row in sorted_employees:
    print(row)
