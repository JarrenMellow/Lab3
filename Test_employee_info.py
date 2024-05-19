import employee_info as employee_info 

def test_get_employees_by_age_range():
    result =[]
    result = employee_info.get_employees_by_age_range(29,31)
    assert result== [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000}]


def test_calculate_average_salary():
    for item in employee_info.employee_data:
        if item["name"] == "John":
            item["salary"] = 3000
            break
    result = employee_info.calculate_average_salary()
    assert(round(result,2)==52333.33)


def test_get_employees_by_dept():
    result =[]
    result = employee_info.get_employees_by_dept("Sales")


    assert result== [{"name": "John", "age": 30, "department": "Sales", "salary": 3000},{"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    


    
    