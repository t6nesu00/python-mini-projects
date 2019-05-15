# list overlap is a program that prints the common characters from two list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

overlaped = []

for n in a:
    if n in a and n in b:
        overlaped.append(n)
print(overlaped)
without_duplicates = []
for n in overlaped:
    if n not in without_duplicates:
        without_duplicates.append(n)
print("The overlapped numbers without duplicates: ")
print(without_duplicates)

