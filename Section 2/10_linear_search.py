def linear_search(array, search):
    for i in range(len(array)):
        if array[i] == search:
            return i
    return -1

grades = [3, 5, 12, 10, 4]
search = 12
result = linear_search(grades, search)

if result == -1:
    print("The value " + str(search) + " is not found in the array.")
else:
    print("The value " + str(search) + " is found at index " + str(result))