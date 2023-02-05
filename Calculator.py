#Calculator
#Addition
def add(num1, num2):
  return num1+num2

#Substraction
def subtract(num1, num2):
  return num1-num2

#Multiplication
def multiply(num1, num2):
  return num1 * num2

#Divison
def divide(num1, num2):
  return num1/num2

#dictionary of operations
operations={'+':add, '-': subtract,'*':multiply, '/': divide}

#Taking User Inputs
num1= int(input("Enter First Number: "))


for o in operations:
  print(o)

operation = input('Enter the operation')

num2= int(input("Enter Second Number: "))
result = operations[operation](num1,num2)
print(f"{num1}{operation}{num2}={result}")
