# =========================================================
# Question 1:
# Write a Python program to find the smallest number in the 
# following list using a for loop.
# my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]
# Print the smallest number as the output.
# =========================================================

my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]

min_val = my_list[0]
for i in my_list:
    if i < min_val:
        min_val = i

print("Smallest number:", min_val)


# =========================================================
# Question 2:
# Write a Python program to find the average of all the numbers 
# in the following list:
# my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]
# Use a for loop to calculate the sum of the numbers and then 
# find and print their average.
# =========================================================

my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]

s = 0
for x in my_list:
    s = s + x

avg = s / len(my_list)
print("Average:", avg)


# =========================================================
# Question 3:
# Create a list of student names:
# students = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal"]
# Ask the user to enter a student name.
# If the name exists, display: Student Found
# Otherwise: Student Not Found
# =========================================================

students = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal"]

name = input("Enter student name: ")

found = False
for student in students:
    if student == name:
        found = True
        break

if found:
    print("Student Found")
else:
    print("Student Not Found")


# =========================================================
# Question 4:
# Create an empty list:
# shopping = []
# Ask the user to enter 5 shopping items.
# Then display the complete shopping list.
# =========================================================

shopping = []

for i in range(5):
    item = input("Enter item: ")
    shopping.append(item)

print("Shopping list:", shopping)
