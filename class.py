class Student:
    def __init__(self, name: str, year: str, department: str):
        self.name = name
        self.year = year
        self.department = department
    
    def display(self):
        print(self.name, "pursuing", self.year, "Engineering and currently at", self.year, "year")

s1 = Student("Iyynes", "3rd", "Mechanical")
s1.display()