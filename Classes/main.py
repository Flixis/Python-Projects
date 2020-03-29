class Employee:
    
    raise_amount = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    def get_all_info(self):
        return 'FirstName: {} \n LastName: {} \n E-Mail: {} \n Pay: {}'.format(self.first,self.last,self.email,self.pay)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp1 = Employee('Tuna','Fish',42069)
emp2 = Employee('Dog','Animal',69420)

mng1 = Manager('Sue', 'Smith', 90000, [emp1])

print(emp1.email)
print(emp2.email)
print(Employee.get_all_info(emp1))
print(mng1.email)
#print(help(Employee))