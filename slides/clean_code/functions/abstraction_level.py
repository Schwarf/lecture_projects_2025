def calculate_salaried_pay(employee):
    pass


def calculate_hourly_pay(employee):
    pass



# BAD: Mixed levels of abstraction
def calculate_payroll(employees):
    for employee in employees:
        if employee.is_salaried:
            calculate_salaried_pay(employee)
        else:
            calculate_hourly_pay(employee)
        # Save payroll info to database (low-level detail)
        db.save(employee) # <---- BAD 



# GOOD: Separate high-level and low-level logic
def calculate_payroll(employees):
    for employee in employees:
        calculate_employee_pay(employee)

def calculate_employee_pay(employee):
    if employee.is_salaried:
        calculate_salaried_pay(employee)
    else:
        calculate_hourly_pay(employee)
