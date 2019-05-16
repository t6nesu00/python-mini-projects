# program to check the string is a palindrome or not.

user_string = input("Give your string: ")
# for reversing the string
reverse_string = user_string[::-1]
if user_string == reverse_string:
    print("This", user_string, "is a palindrome word.")

# created by Suman Nepali May, 2019
