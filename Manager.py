from Employee import Employee


class Manager(Employee):

    def __init__(self, id_, name, address, age, number_of_employees, hours_rate):
        super().__init__(id_, name, address, age)
        self.number_of_employees = number_of_employees
        self.hours_rate = hours_rate

    def calculate_salary(self):
        return self.number_of_employees * self.hours_rate

    def __str__(self):
        return f'Worker[number_of_employees = {self.number_of_employees}, ' \
        f'hours_rate = {self.hours_rate}' + '|' + super().__str__()

