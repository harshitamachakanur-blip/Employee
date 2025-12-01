def employee_info(name, emp_id, department, salary):
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )

if _name_ == "_main_":
    name = "Rahul"
    emp_id = "EMP1024"
    department = "Finance"
    salary = 45000
    
    print("Employee Details:\n")
    print(employee_info(name, emp_id, department, salary))
