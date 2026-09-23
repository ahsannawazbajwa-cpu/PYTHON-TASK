# ==========================================
# Question No. 1
# Ask the user for the marks of 5 subjects.
# Calculate Total Marks, Percentage, Grade and Pass/Fail.
# ==========================================

total = 0

for i in range(5):
    marks = float(input("Enter marks of subject " + str(i + 1) + ": "))
    total = total + marks

percentage = (total / 500) * 100

if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if percentage >= 50:
    result = "Pass"
else:
    result = "Fail"

print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)


# ==========================================
# Question No. 2
# Take a student's name and display:
# Uppercase, Lowercase, Number of Characters,
# First Character and Last Character
# ==========================================

name = input("\nEnter student's name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Number of characters:", len(name))
print("First character:", name[0])
print("Last character:", name[-1])


# ==========================================
# Question No. 3
# Ask the user to enter 10 numbers.
# Calculate Sum, Average, Largest, Smallest,
# Even Numbers and Odd Numbers.
# ==========================================

numbers = []

for i in range(10):
    num = int(input("\nEnter number " + str(i + 1) + ": "))
    numbers.append(num)

total = sum(numbers)
average = total / 10
largest = max(numbers)
smallest = min(numbers)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("\nSum:", total)
print("Average:", average)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)


# ==========================================
# Question No. 4
# Create a simple ATM program.
# Starting Balance = 50000
# ==========================================

balance = 50000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance = balance + amount
        print("Amount deposited successfully.")
        print("New balance:", balance)

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful.")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance.")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please try again.")


# ==========================================
# Question No. 5
# Ask the user for a number n and print
# multiplication tables from 1 to n.
# ==========================================

n = int(input("\nEnter a number: "))

for i in range(1, n + 1):
    print("\nTable of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
