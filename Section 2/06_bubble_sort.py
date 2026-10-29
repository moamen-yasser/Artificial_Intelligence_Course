grades = [10, 5, 6, 20, 15, -3, 5] # => [-3, 5, 5, 6, 10, 15, 20]
print(grades)

#Bubble Sort Algorithm

for i in range(len(grades) - 1):
    for j in range(len(grades) - i - 1):
        if grades[j] > grades[j + 1]:
            grades[j], grades[j + 1] = grades[j + 1], grades[j]

print(grades)
print("Highest Grade:", grades[-1])
print("Lowest Grade:", grades[0])