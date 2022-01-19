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


class programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.exp = exp

    def increase(self):
        self.salary = int(self.salary * (self.increment+0.2))
        return self.salary

rahmat = programmer('rahmat', 'ullah', 99000, 'python', '5 years')
print(rahmat.increase())

# shubham = Employee('shubham', 'jackson', 88000)
# print(shubham.isopen('sunday'))
# murad = Employee('murad', 'khan', 44000)
# prince = Employee('prince', 'jack', 74000)
# imteyaz = Employee('imteyaz', 'khan', 44000)
# lovish = Employee.from_str("lovish-jackson-76000")

# print(lovish.salary)
# print(murad.salary)
# Employee.change_increment(3)
# murad.increase()
# print(murad.salary)



# print(Employee.__dict__)
# print(murad.fname, prince.fname)