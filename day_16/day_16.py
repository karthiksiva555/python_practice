from prettytable import PrettyTable
# Using Turtle and Screen classes
from turtle import Turtle, Screen
from employee import Employee


# tommy = Turtle()
# print(tommy)
# tommy.shape('turtle')
# tommy.color("cyan")
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.canvwidth = 400
# my_screen.exitonclick()

#installing PrettyTable package from PyPi (Python Package Index)
table = PrettyTable()
print(table)

#change the alignment
table.align = "l"

table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])
print(table)

# create employee object
robert = Employee("robert")
robert.first_name = "Robert"
print(robert.first_name)
try:
    robert.first_name = ""
    print(robert.first_name)
except ValueError as ex:
    print(ex)


class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

employees = [
    Employee("Ram", 123),
    Employee("John", 234)
]

employee_ram_exists = any("Ram" == employee.name for employee in employees)
print(employee_ram_exists)
employee_ram = next((employee for employee in employees if employee.name == "Ram"), None)
print(f"{employee_ram.name}, {employee_ram.number}")






