from functools import reduce

def add_function(a, b):
    return a + b
print(add_function(2, 3))

add_lambda = lambda x, y : x + y
print(add_lambda(5,9))

#Using Lambda with Built-In Functions
#1- with map()
numbers = [1, 2, 3]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

#2- with filter()
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

#3- with sorted()
data = [(1, 'B'), (3, 'C'), (2, 'A')]
sorted_data = sorted(data, key = lambda x: x[0])
print(sorted_data)

#4-with multiple iterabled in map()
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
added_numbers = list(map(lambda x, y: x + y, numbers1, numbers2))
print(added_numbers)

#5-with reduce()
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

sum = reduce(lambda x, y: x + y, numbers)
print(sum)

max = reduce(lambda x, y: x if x > y else y, numbers)
print(max)