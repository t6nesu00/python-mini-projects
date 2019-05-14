from datetime import date

user_name = input("What is your good name?: ")
user_age = int(input("What is your age?: "))

gap_to_be_hundred = 100 - user_age

# date.today().year gives current year
hundred_in = date.today().year + gap_to_be_hundred
print("Hello", user_name, "you will be 100 years old in", hundred_in)

# created by Suman Nepali May, 2019


