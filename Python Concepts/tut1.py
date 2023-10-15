class Employee:
    no_of_leaves=30
    role="Developer"

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def printDet(self):
        print(f"My name is {self.name}.I have a salary of {self.salary}.Role is {self.role}")

    #Class methods changes the variables of class by help of instances.
    @classmethod
    def Changeleaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    #making constructor with help of class meyhod
    @classmethod
    def from_str(cls,str):
        params=str.split("-")
        return cls(params[0],params[1],params[2])


suyog=Employee("Sonu",50000,"QA Tester")
# ashish=Employee()
suyog.printDet()
suyog.name="Suyog"
suyog.salary=600000
# ashish.name="Ashish"
# ashish.salary=900000
print(suyog.no_of_leaves)
print(Employee.__dict__)
suyog.Changeleaves(50)
print(f"Employees leaves are {Employee.no_of_leaves}.")
suyog.printDet()
ashish=Employee.from_str("Ashish-79000-Manager")
ashish.printDet()