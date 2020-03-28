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

emp1 = Employee('Tuna','Fish',42069)
emp2 = Employee('Dog','Animal',69420)

print(emp1.email)
print(emp2.email)
print(Employee.get_all_info(emp1))