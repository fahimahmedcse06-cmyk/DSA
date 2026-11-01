def linear_search(arr, target):
    # Loop through the entire array
    for i in range(len(arr)):
        # If element is found, return its index
        if arr[i] == target:
            return i
    # Return -1 if the target is not in the array
    return -1

# Driver code to test the function
numbers = [10, 23, 45, 70, 11, 15]
target_val = 70

result = linear_search(numbers, target_val)
print("Index found at:", result)
