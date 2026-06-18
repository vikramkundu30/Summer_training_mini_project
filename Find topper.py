n=[]
r=[]
m=[]
student={
    "Name":n,
    "Roll no.":r,
    "Marks":m
}
y=int(input("Enter the no. of student database you have to enter = "))
for i in range(y):
    n.append(str(input("Enter the name = ")))
    r.append(int(input("Enter the roll no. = ")))
    m.append(int(input("Enter the marks = ")))
print(student)
m.sort()
print(m[-1])
