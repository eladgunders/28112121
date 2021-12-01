from Employee import Employee


class Worker(Employee):

    def __init__(self, id_, name, address, age, hours_per_day, hours_rate):
        super().__init__(id_, name, address, age)
        self.hours_per_day = hours_per_day
        self.hours_rate = hours_rate

    def calculate_salary(self):
        return self.hours_per_day * self.hours_rate

    def __str__(self):
        return f'Worker[hours_per_day = {self.hours_per_day}, hours_rate = {self.hours_rate}'+'|'+super().__str__()
