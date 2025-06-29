class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f"Employee {self.name} on position {self.position} with salary {self.salary} rub."
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.position})"
    

class Developer(Employee):
    def __init__(self, name, position, salary, programming_language):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self):
        return f"Developer {self.name} on position {self.position} " \
               f"with salary {self.salary} rub. using {self.programming_language}"
    

class Manager(Employee):
    def __init__(self, name, position, salary, employees):
        super().__init__(name, position, salary)
        self.employess = employees

    def get_info(self):
        return f"{self.position} {self.name} with salary {self.salary} " \
               f"responsible for {', '.join(str(employee) for employee in self.employess)}"

    
e = Employee("Sasha", "QA Engineer", 100000)
d = Developer("Denis", "Backend Dev", 210000, "Python")
m = Manager("Billy", "Product Manager", 300000, [e, d])
print(m.get_info())