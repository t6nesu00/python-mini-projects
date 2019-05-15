# program that asks the user for a number and then prints out a list of all the divisors of that number.

print("Hello I can give you the divisors of the number.")
user_number = int(input("Give the number: "))
divisors_of_number = []
numbers_for_division = range(1, user_number+1)

for number in numbers_for_division:
    if user_number % number == 0:
        divisors_of_number.append(number)
print("These", len(divisors_of_number), "numbers are the divisors of", user_number)
print(divisors_of_number)

# created by Suman Nepali, May, 2019
