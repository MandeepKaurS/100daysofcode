from art import logo
#Calculator
#Addition
def calculator():
  print(logo)
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
  num1= float(input("Enter first Number: "))
  
  user_input=True
  while(user_input==True):
  #Taking User Inputs
    
    for o in operations:
      print(o)
    
    operation = input('Enter the operation')
    
    num2= float(input("Enter next Number: "))
    result = operations[operation](num1,num2)
    print(f"{num1}{operation}{num2}={result}")
    
    continueCalc=input(f" Type \'y\' to continue calculating with {result} or type \'n\' to start a new calculation. :")
    if continueCalc=="n":
      user_input=False
      calculator()
    else:
      num1=result
      continue
calculator()
      
