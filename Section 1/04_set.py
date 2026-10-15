#Create Set
s1 = {1, 2, 3, 4}
print(f"Set S1 {s1}") #Output Set S1 {1, 2, 3, 4}

#Sorted & No Duplicates
s2 = {2, 4, 6, 1, 2, 3, 6}
print(f"Set S2 {s2}") #Output Set S1 {1, 2, 3, 4, 6}

s3 = {'A', 'B'}
print(f"Set S3 {s3}") # The output may appear as {'A', 'B'} or {'B', 'A'}
                    # depending on how Python stores the elements internally using a hash table.
# If you want to display the elements in a specific order,
# convert the set to a list or use the sorted() function:
print("Sorted S3", sorted(s3))  # Output: ['A', 'B']

#Adding element to the set
s4 = {'A', 'B'}
s4.add('C')
print(f"Set S4 {s4}")

# A set can store heterogenous elements
s5 = {"A", "b", -5, 3.7, True}
print(f"Set S5 {s5}")  # Output: {True, 3.7, 'A', 'b', -5}

#Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}

# Clearing of set
s6 = {1,2,3,4,5,6}
s6.clear()
print(f"Set S6 {s6}")

f = frozenset(['A', 'B', 'C'])
f.add('D') #AttributeError: 'frozenset' object has no attribute 'add'