# Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.
class Employee:
  def __init__(self, name, title, start_date):
    self.name = name
    self.job_title = title
    self.start_date = start_date

# Copy the Company class into your module.

# Consider the concept of aggregation (item should exist if the super is gone), and modify the Company class so that you assign employees to a company.
class Company:
  """This represents a company in which people work"""

  def __init__(self, company_name, date_founded):
    self.company_name = company_name
    self.date_founded = date_founded
    self.employees = set() # here's the modification

  def get_company_name(self):
    """Returns the name of the company"""
    return self.company_name

  def add_employee(self, employee):
    self.employees.add(employee)

  def __str__(self):
    temp = [f'{emp.name}' for emp in self.employees]
    return f'{(", ").join(temp)} work at {self.company_name}, which was founded on {self.date_founded}.'

# Create a company, and three employees, and then assign the employees to the company.
zac = Employee('Zac', 'CFO (Chief Fryer Officer)', '1-1-2019')
brendan = Employee('Brendan', 'CEO (Chief Eating Officer)', '1-2-2019')
ousama = Employee('Ousama', 'CSO (Chief Sauce Officer)', '1-3-2019')

chick_fil_a = Company('Chick fil A', '1-1-1950')

chick_fil_a.add_employee(zac)
chick_fil_a.add_employee(brendan)
chick_fil_a.add_employee(ousama)

print(chick_fil_a)

# PRINT RESULT: Brendan, Zac, Ousama work at Chick fil A, which was founded on 1-1-1950.