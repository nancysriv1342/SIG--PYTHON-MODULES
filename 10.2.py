
class stud:
    def __init__(self, roll,name):
        self.roll=roll
        self.name=name
def display(self):
    print(self.roll,self.name,self.age,self.marks)
def setAge(self):
    self.age=int(input("Enter age : "))
def setMarks(self):
    self.marks=int(input("Enter marks : "))
    s1=stud(111,"udit")
    s2=stud(222,"pram")
    s1.setAge()
    s1.setMarks()
    s2.setAge()
    s2.setMarks()
    s1.display()
    s2.display()