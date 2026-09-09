# Question 1: Write a Python program that takes the user's name as input and then prints a greeting message like "Hello, Ali".
name = input("Enter your name: ")
print(f"Hello, {name}")

# Question 2: Write a Python program that takes hours worked and hourly rate as input from the user, then calculates and displays the gross pay.
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
gross_pay = hours * rate
print(f"Gross Pay: {gross_pay}")

# Question 3: Write a Python program that takes temperature in Celsius as input from the user and converts it to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

# Question 4: Write a Python program that takes two numbers as input and calculates the first number raised to the power of the second number (exponentiation).
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 ** num2
print(f"Result: {result}")

# Question 5: What does the following Python code do? Explain the type conversion that happens in this program.
age = 20
item = 5
print("age : ", age)
print("items : ", item)

age = float(age)
item = float(item)
print("age : ", age)
print("items: ", item)
