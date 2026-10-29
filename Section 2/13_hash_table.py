person = {'name': 'Moamen', 'age': 24, 'city': 'Cairo', 'country': 'Egypt', 'gender': 'Male'}

print(person)
print(person['name'])
print(person['age'])
print(person['city'])
print(person['country'])
print(person['gender'])

person['age'] = 25
print(person['age'])

persons = [
    {'name': 'Moamen', 'age': 24, 'city': 'Cairo', 'country': 'Egypt', 'gender': 'Male'},
    {'name': 'Ahmed', 'age': 30, 'city': 'Alexandria', 'country': 'Egypt', 'gender': 'Male'},
    {'name': 'Sara', 'age': 21, 'city': 'Giza', 'country': 'Egypt', 'gender': 'Female'}

]

print(persons[2]['name'])

for i in range(len(persons)):
    print(persons[i]['name'])