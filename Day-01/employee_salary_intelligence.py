employees = [
    {"name": "A", "dept": "IT", "salary": 50000},
    {"name": "B", "dept": "HR", "salary": 35000},
    {"name": "C", "dept": "IT", "salary": 75000},
    {"name": "D", "dept": "HR", "salary": 45000},
    {"name": "E", "dept": "IT", "salary": 60000},
    {"name": "F", "dept": "Sales", "salary": 40000}
]


#Q1. Calculate average salary for each department.
department_data = {}

for i in employees:
    if i["dept"] not in department_data:
        department_data[i["dept"]] = {"total_salary": 0,"total_employee": 0}
    department_data[i["dept"]]["total_salary"] += i["salary"]
    department_data[i["dept"]]["total_employee"] += 1

for dept, data in department_data.items():
    average_salary = data["total_salary"] / data["total_employee"]
    print(dept,": Average Salary = ",average_salary)



#Q2. Find the highest-paid employee in each department.
department_data= {}

for i in employees:
    if i["dept"] not in department_data:
        department_data[i["dept"]] = {"name":"","salary":0}

    if i["salary"] > department_data[i["dept"]]["salary"]:
        department_data[i["dept"]]["name"] = i["name"]
        department_data[i["dept"]]["salary"] = i["salary"]

print(department_data)



#Q3. Find employees earning above their department's average.
department_data = {}
department_avg = {}

for i in employees:
    dept = i["dept"]
    if i["dept"] not in department_data:
        department_data[i["dept"]] = {"total_salary":0,"total_employee":0}
    department_data[i["dept"]]["total_salary"] += i["salary"]
    department_data[i["dept"]]["total_employee"] += 1

for dept, data in department_data.items():
    average_salary = data["total_salary"] / data["total_employee"]
    department_avg[dept] = average_salary
    
for i in employees:
    if i["salary"] > department_avg[i["dept"]]:
        print(i["name"], ":", i["salary"], "(", i["dept"], ")")



#Q4. Rank employees within each department by salary.
def rank_employees(employees):
    department_data = {}

    for i in employees:
        dept = i["dept"]
        if dept not in department_data:
            department_data[dept] = []
        department_data[dept].append(i)

    for dept, data in department_data.items():
        print("\n", dept)
        sorted_employees = sorted(data,key=lambda x: x["salary"],reverse=True)
        for rank, employee in enumerate(sorted_employees, start=1):
            print(rank, employee["name"], employee["salary"])

rank_employees(employees)



#Q5. Return the department with the highest average
department_data = {}
highest_dept = 0
best_department = ""

for i in employees:
    dept = i["dept"]
    if dept not in department_data:
        department_data[dept] = {"total_salary": 0,"total_employee": 0}
    department_data[i["dept"]]["total_salary"] += i["salary"]
    department_data[dept]["total_employee"] += 1

for dept, data in department_data.items():
    average_salary = data["total_salary"] / data["total_employee"]
    department_data[dept]["average_salary"] = average_salary

for dept, data in department_data.items():
    if data["average_salary"] > highest_dept:
        highest_dept = data["average_salary"]
        best_department = dept

print(best_department, highest_dept)