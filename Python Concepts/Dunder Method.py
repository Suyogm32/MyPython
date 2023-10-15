class Emp:
    no_of_leaves=27
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def printDet(self):
        return f"My name is {self.name}.I have a salary of {self.salary}.Role is {self.role}"

    @classmethod
    def Changeleaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    # making constructor with help of class meyhod
    @classmethod
    def from_str(cls, str):
        params = str.split("-")
        return cls(params[0], params[1], params[2])

    def __add__(self, other):
        return self.salary+other.salary

    def __repr__(self):
        return  self.printDet()



#the methods sdtarts with '__' and end with '__' are known as dunder methods example. __init__()

emp1=Emp("luv",450,"Dev")
emp2=Emp("Kush",550,"QA Tester")
print(emp1+emp2)

print(emp1)