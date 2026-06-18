c=[]
r=[]
m=[]
s={
    "Name":c,
    "Roll no.":r,
    "Marks":m
}
c.append(input("Enter the name = "))
r.append(input("Enter the roll no. = "))
m.append(input("Enter the marks = "))
print(s)
i = input("Enter the name to update = ")
if i in c:
    index = c.index(i)
    c[index] = input("Enter new name = ")

j = input("Enter the roll no. to update = ")
if j in r:
    index = r.index(j)
    r[index] = input("Enter new roll no. = ")

k = int(input("Enter the marks to update = "))
if k in m:
    index = m.index(k)
    m[index] = int(input("Enter new marks = "))

print("Updated Data:")
print(s)
sn = input("Enter the name to search = ")
if sn in c:
    print("Name found")
else:
    print("Name not found")
m.sort()
x = m[-1]

print("Highest Marks =", x)