from Employee import Employee


class Contractor(Employee):

    def __init__(self, id_, name, address, age, num_of_projects, proj_rate):
        super().__init__(id_, name, address, age)
        self.num_of_projects = num_of_projects
        self.proj_rate = proj_rate

    def calculate_salary(self):
        return self.num_of_projects * self.proj_rate

    def __str__(self):
        return f'Worker[num_of_projects = {self.num_of_projects}, ' \
               f'proj_rate = {self.proj_rate}' + '|' + super().__str__()