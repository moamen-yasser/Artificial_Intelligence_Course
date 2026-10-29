#Tuple is Immutable, meaning that you cannot change the values of a tuple after it has been created.

grades = (10, 15, 20)

print(grades)
print(grades[0])
print(grades[1])
print(grades[2])

grades[0] = 5 # => TypeError: 'tuple' object does not support item assignment