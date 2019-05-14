# program that tells the number is odd or even

user_number = int(input("Please give a number: "))
if user_number == 0:
    print("Sorry! zero is neither odd nor even.")
elif user_number % 2 == 0:
    print(user_number, "is even.")
else:
    print(user_number, "is odd.")

# created by Suman Nepali May, 2019