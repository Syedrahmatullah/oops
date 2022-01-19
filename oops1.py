#Dunder Method

class Employee:

    increment = 1.5
    no_of_employees = 0
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees +=1

    def increase(self):
        self.salary = int(self.salary * self.increment)

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

    @staticmethod
    def isopen(day):
        if day == "sunday":
            return False
        else:
            return True

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return 'Employee ({}, {}, {})'. format(self.fname, self.lname, self.salary)

    def __str__(self):
        return 'The name of employee is {}'.format(self.fname)

rahmat = Employee('rahmat', 'ullah', 99000)
rohan = Employee('rohan', 'agarwal', 9)

print(repr(rahmat))