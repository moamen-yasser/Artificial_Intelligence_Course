#Empty Tuple
t1 = ()
print(f"Tuple T1: {t1}")

#Mixed Tuple
t2 = (1, "A", 2, "d", 4)
print(f"Tuple T2: {t2}")

#Tuple From List
t3 = tuple([1, 2, 3, 4])
print(f"Tuple T3: {t3}")

#Tuple Unpacking
t4 = (10, 20, 30)  
x, y, z = t4
print(f"Tuple T4: {t4}")
print(f"Unpacked values: {x}, {y}, {z}")

#Attempting to modify a tuple (will raise an error)
t5 = (1, "A", 2)
t5[1] = 10 #TypeError: 'tuple' object does not support item assignment
print(f"Modified Tuple T5: {t5}") 

#Deleting a tuple
t6 = (0, 1, 2, 3, 4)
del t6
print(f"Deleted Tuple T6: {t6}")  # This line will raise a NameError: name 't6' is not defined