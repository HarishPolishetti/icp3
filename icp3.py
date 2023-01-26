class Employee:
    count = 0
    salary_cnt = 0
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.count += 1
        Employee.salary_cnt = Employee.salary_cnt + salary

    def average_salary(self):
        return Employee.salary_cnt/Employee.count


class FulltimeEmployee(Employee):
    pass

fulltime_employee1 = FulltimeEmployee("Gorden", "Ramsay", 12000, "administration")
fulltime_employee2 = FulltimeEmployee("Jhonson", "Dwayne", 10000, "HR")
print("Fulltime Employees average salary using member function: {}".format(
    fulltime_employee2.average_salary()))
employee1 = Employee("John", "cena", 6000, "IT")
employee2 = Employee("Jane", "mikey", 8000, "IT")
print("Employees average salary using member function: {}".format(
    employee1.average_salary()))
