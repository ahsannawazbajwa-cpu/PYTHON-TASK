#QUESTION NO .  1 pay calculator.py


hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours <= 40:
    total_pay = hours * rate
else:
    overtime_hours = hours - 40
    total_pay = (40 * rate) + (overtime_hours * rate * 1.5)

print(f"Total Pay: {total_pay:.2f}")

#QUESTION marksheet

name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")

# Prompt requires 5 subjects
subjects = [
    "DLD (Digital Logic Design)",
    "E.W (Expository Writing)",
    "OOP (Object Oriented Programming)",
    "IoT (Internet of Things)",
    "M-II (Mathematics-II)"
]

marks = []
for subj in subjects:
    m = float(input(f"Enter marks for {subj}: "))
    marks.append(m)

num_subjects = len(subjects)
total = sum(marks)
percentage = total / num_subjects

if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Check if student failed in any subject
failed_subject = any(m < 40 for m in marks)

if failed_subject or percentage < 40:
    result = "Fail"
else:
    result = "Pass"

print("\n" + "="*35)
print("            MARKSHEET")
print("="*35)
print(f"Name       : {name}")
print(f"Roll No    : {roll_no}")
print("-" * 35)
for subj, m in zip(subjects, marks):
    print(f"{subj:<25}: {m}")
print("-" * 35)
print(f"Total      : {total} / {num_subjects * 100}")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")
print(f"Result     : {result}")
print("="*35)









