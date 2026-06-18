import csv

students_raw_data = [
    ["Aarav", 85, 90, 88], ["Vivaan", 78, 82, 80], ["Aditya", 92, 95, 91],
    ["Vihaan", 65, 70, 68], ["Arjun", 89, 91, 94], ["Sai", 72, 75, 74],
    ["Reyansh", 95, 96, 97], ["Krishna", 81, 85, 83], ["Ishaan", 60, 62, 65],
    ["Shaurya", 88, 87, 89], ["Diya", 90, 92, 93], ["Ananya", 84, 86, 85],
    ["Aadhya", 77, 79, 78], ["Pari", 83, 85, 84], ["Avani", 91, 89, 92],
    ["Saanvi", 69, 71, 70], ["Myra", 76, 78, 77], ["Anika", 94, 93, 95],
    ["Riya", 82, 80, 81], ["Aaliyah", 87, 88, 86]
]

headers = ["Name", "Python", "ML", "AI", "Total_Marks"]
with open("aiml_students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for student in students_raw_data:
        name = student[0]
        python_marks = student[1]
        ml_marks = student[2]
        ai_marks = student[3]
        total = python_marks + ml_marks + ai_marks
        row = [name, python_marks, ml_marks, ai_marks, total]
        writer.writerow(row)
print("CSV file 'aiml_students.csv' has been created.")
highest_score = 0
topper_name = ""
with open("aiml_students.csv", mode="r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        current_name = row[0]
        current_total = int(row[4])
        if current_total > highest_score:
            highest_score = current_total
            topper_name = current_name
print("\n--- Class Topper Result ---")
print("Name: ", topper_name)
print("Total Marks: ", highest_score, "/ 300")
