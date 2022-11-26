# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
two_digit_number=int(two_digit_number)

digit1 = two_digit_number%10

digit2 = int((two_digit_number-digit1)/10)

print( digit1+digit2)
