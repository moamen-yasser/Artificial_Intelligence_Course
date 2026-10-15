#Empty dictionary
d1 = {}
print(f"Dictionary D1: {d1}")  # Output: {}

#Dictionary with integer keys
d2 = {3: "A", 10: "B", 20: "C"}
print(f"Dictionary D2: {d2}")  # Output: {3: 'A', 10: 'B', 20: 'C'}
print(f"Value for key 10 in D2: {d2[10]}")  # Output: Value for key 10 in D2: B

#Create a dictionary with mixed keys
d3 = {'name': "Mohamed", 1: [1, 2, 3, 4]}
print(d3['name']) # Output: Mohamed
print(d3[1])  # Output: [1, 2, 3, 4]

#Creating a dictionary with each item as a pair
d4 = dict([(1, "A"), (2, "B")])
print(f"Dictionary D4: {d4}")  # Output: {1: 'A', 2: 'B'}

#Nested Dictionary
d5 = {1: 'A', 2: 'B', 3: {'x': 10, 'y': 20}}
print(d5[3]['x']) #Output 10

d6 = {'A': 90, 'B': 80, 'B': 70}
del d6['B']
print(f"Dictionary D6 {d6}")

#Add elements dynamically
d7 = {}
d7['x'] = 10
d7['y'] = 5, 6, 7
print(f"Dictionary D7 {d7}") #Output {'x': 10, 'y': (5, 6, 7)}

#Copying VS. Referencing
x = {1: 'A', 2: 'B'} 
y = x
z = x.copy()

x[3] = 'C'
y[4] = 'D'
z[10] = 'J'

print(x) #Output {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
print(y) #Output {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
print(z) #Output {1: 'A', 2: 'B', 10: 'J'}