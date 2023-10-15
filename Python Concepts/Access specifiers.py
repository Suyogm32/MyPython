#There are 3 access specifiers 1)Public, 2)Private, 3)Protected

class Employee:
    no_of_leaves=30
    #To create a protected variable we use one '_' before variable name. as shown role is a protected variable
    _role="Developer"
    #To create a private variable we use '__' before the variable as shown
    __team_name="Alpha"


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

kush=Employee("Kush",50000,"Team Lead")

print(kush._role)
print(kush._Employee__team_name)