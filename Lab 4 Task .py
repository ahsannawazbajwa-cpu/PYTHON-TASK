# Question 1:
# Ask the user for Name, Age, Program and Marks.
# Store the information in a tuple.

name = input("Name: ")
age = int(input("Age: "))
program = input("Program: ")
marks = int(input("Marks: "))

student = (name, age, program, marks)
print(student)


# Question 2:
# Ask the user to enter a sentence.
# Display the number of characters, words, vowels, spaces and digits.

s = input("Enter sentence: ")

v = sp = d = 0

for x in s:
    if x in "aeiouAEIOU":
        v += 1
    elif x == " ":
        sp += 1
    elif x.isdigit():
        d += 1

print("Characters:", len(s))
print("Words:", len(s.split()))
print("Vowels:", v)
print("Spaces:", sp)
print("Digits:", d)


# Question 3:
# Ask the user to enter information for 3 employees:
# Name, Age and Salary.
# Store each employee's information in a tuple
# and store all tuples in a list.

employees = []

for i in range(3):
    name = input("Name: ")
    age = int(input("Age: "))
    salary = int(input("Salary: "))
    employees.append((name, age, salary))

print(employees)


# Question 4:
# Given the tuple:
# numbers = (10, 15, 20, 25, 30, 35, 40)
# Use a loop to count the even and odd numbers.

numbers = (10, 15, 20, 25, 30, 35, 40)

even = odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
