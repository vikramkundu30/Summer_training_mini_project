def student_result():
    name = input("Enter student name: ")
    subjects = ["Physics", "Math", "Chemistry", "English", "Biology"]
    marks = [85,65,66,75,78]
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    is_pass = all(mark >= 33 for mark in marks)
    final_result = "PASS" if is_pass else "FAIL"
    if final_result == "FAIL":
        grade = "F"
    elif percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "E"
    print("\n" + "="*30)
    print(f"      REPORT CARD: {name.upper()}      ")
    print("="*30)
    print(f"Total Marks : {total_marks:.2f} / 500")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")
    print(f"Final Result: {final_result}")
    print("="*30)
if __name__ == "__main__":
    student_result()
