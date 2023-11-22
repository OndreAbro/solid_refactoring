class Employee:
    def __init__(self, name, dob, base_salary):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"


class Account:
    @staticmethod
    def calculate_net_salary(employee):
        tax = int(employee.base_salary * 0.25)  # рассчитать налог другим способом
        return emloyee.base_salary - tax
