# Question 1: Find unique elements in A and B.
# Also find common elements, difference and symmetric difference.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Common Elements:", A & B)
print("A - B:", A - B)
print("B - A:", B - A)
print("Symmetric Difference:", A ^ B)


# Question 2: Write a function to calculate the factorial.

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))


# Question 3: Write a function using keyword arguments to display student information.

def student_info(name, age, department):
    print("Student Name:", name)
    print("Age:", age)
    print("Department:", department)

student_info(name="Ahsaan", age=20, department="Artificial Intelligence")


# Question 4: Write a function using *args to calculate the sum of multiple numbers.

def total_sum(*numbers):
    total = 0

    for num in numbers:
        total = total + num

    return total

result = total_sum(10, 20, 30, 40, 50)
print("Total Sum:", result)


# Question 5: Write a function using **kwargs to display employee information.

def employee_info(**details):
    for key, value in details.items():
        print(key, ":", value)

employee_info(name="Ali", age=25, salary=30000, department="IT")


# Question 6: Create a function to check whether a password is valid.

def check_password(password):

    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(not char.isalnum() for char in password):
        return False

    return True

password = input("Enter your password: ")

if check_password(password):
    print("Password is valid")
else:
    print("Password is not valid")
