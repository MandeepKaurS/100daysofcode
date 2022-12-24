bill = int(input("Enter your total bill?"))
tax = 0.13 * bill
print(f"your tax is {round(tax, 3)}")
print(f"your total bill including taxes is {bill+tax}")
