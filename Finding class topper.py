class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_details(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
class student(person):
    def __init__(self,name,age,roll_no,marks):
        person.__init__(self,name,age)
        self.roll_no=roll_no
        self.marks=marks
    def display_details(self):
        person.display_details(self)
        print(f"Roll No : {self.roll_no}")
        print(f"Marks   : {self.marks}")
students = [
    student("Amit", 19, 622, 85),
    student("Bhavna", 19, 623, 92),
    student("Chetan", 19, 624, 78),
    student("Divya", 19, 625, 95),
    student("Umesh", 19, 626, 88),
    student("Vineet", 19, 627, 64),
    student("Waseem", 19, 628, 71),
    student("Xavier", 19, 629, 90),
    student("Yash", 19, 630, 83),
    student("Zoya", 19, 631, 89),
]
topper = max(students, key=lambda s: s.marks)
print("--- Details of All 10 Students ---")
for s in students:
    s.display_details()
    print("-" * 20)
print("\n=== TOPPER DETAILS ===")
topper.display_details()
