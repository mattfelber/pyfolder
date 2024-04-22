from datetime import *

class Employee:
    num_of_employees = 0
    raise_amt = 1.04


    def __init__(self, first, last, pay):  # Regular Methods take the instance as the first argument (self)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_employees += 1 
                                            # 
 
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) 
                                             # Employee.raise_amount also works. raise_amount on its own it doesnt

    @classmethod
    # sets the raise amount for employees
    def set_raise_amt(cls, amount):          # Class Methods take the class as the first argument (cls) 
        cls.raise_amt = amount

    @classmethod
    # parses through employee strings
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    
    @staticmethod                           
    # takes a date and determines if it's a workday. Used like an alternative constructor
    def is_workday(day):                      # Static methods don't pass anything automatically.
        if day.weekday() == 5 or day.weekday() == 6:
            return False                      # Static methods don't operate on the class or instance.
        return True


emp_1 = Employee('Corey', 'Shafer', 5000)
emp_2 = Employee('Test', 'User', 6000)


import datetime
my_date = datetime.date(2024, 4, 21)

print(Employee.is_workday(my_date))
print(my_date.weekday())

#emp_str_1 = 'John-Doe-7500'
#new_emp_1 = Employee.from_string(emp_str_1)
#print(new_emp_1.email)
#print(new_emp_1.pay)
#emp_3 = Employee('Jon', 'Bones', 8000)
# emp_3.raise_amount = 1.05                   # The class variable remained the same at 1.04, when printing the class variable.
#Employee.set_raise_amt(1.06)                
#print(Employee.raise_amt)
#print(emp_1.raise_amt)                       # From the instance, calling the atribute, checking if that instance contains it.
#print(emp_2.raise_amt)                       # Then if the class or any class it inherits from contains the attribute.
#print(emp_3.raise_amt)                   
#print(Employee.fullname(emp_1))              # Calling the method on the class, you need to specify the instance.
#print(emp_1.fullname())                      # This is an instance where you call the class. no arguments needed