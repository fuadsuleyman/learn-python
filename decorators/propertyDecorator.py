class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('Vasif', 'Qarayev')

#setter
emp_1.fullname = "Fuad Suleymanov"

print(emp_1.first)

# with decorator we use method as property
print(emp_1.email)

# with decorator we use method as property
print(emp_1.fullname)

# delete
del emp_1.fullname
