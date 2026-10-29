def binary_search(array, search):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid  = (left + right) // 2
        if array[mid] == search:
            return mid
        elif array[mid] < search:
            left = mid + 1
        else:
            right = mid - 1
    return -1

grades = [10, 12, 14, 15, 17, 19, 20]
search = 20
result = binary_search(grades, search)

if result == -1:
    print("The value " + str(search) + " is not found in the array.")
else:
    print("The value " + str(search) + " is found at index " + str(result))