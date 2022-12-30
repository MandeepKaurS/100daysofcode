# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = (name1 + name2).lower()
digit1=0
digit2=0
for alphabet in "true":
        digit1+=name.count(alphabet)
for alphabet in "love":
        digit2+=name.count(alphabet)

love_score =int(str(digit1)+str(digit2))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >=40 and love_score<=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


