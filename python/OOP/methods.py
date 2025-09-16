#CLASS METHODS
class Employee:
    raise_amount = 1.04  # class variable

    def __init__(self, first, last, pay):
        self.first = first  # instance variable
        self.last = last    # instance variable
        self.pay = pay      # instance variable
        self.email = first + '.' + last + '@company.com'  # instance variable

    def fullname(self):  # instance method
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):  # instance method
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):  # class method
        cls.raise_amount = amount

    @classmethod
    def from_string (cls, emp_str):  # alternative constructor
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))   
    

emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee('Jane', 'Smith', 60000)
emp_str_1 = 'Alice-Johnson-70000'
emp_str_2 = 'Bob-Brown-80000'
new_emp1 = Employee.from_string(emp_str_1)
new_emp2 = Employee.from_string(emp_str_2)
print(new_emp1.email)
print(new_emp2.pay)
