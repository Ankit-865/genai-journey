# 1. Find Maximum Element in a List – O(n)
# O(n) - Linear Time
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

arr = [10, 3, 45, 7, 22]
print("Max Element:", find_max(arr)) 


# 2. Check if a List Contains a Number – O(n)
# O(n) - Linear Time
def contains(arr, target):
    for num in arr:
        if num == target:
            return True
    return False

print("Contains 7:", contains([1, 2, 3, 7, 9], 7))  
print("Contains 5:", contains([1, 2, 3, 7, 9], 5))  



# 3. Binary Search in Sorted List – O(log n)
# O(log n) - Logarithmic Time
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

arr = [1, 3, 5, 7, 9, 11, 13]
print("Binary Search (7):", binary_search(arr, 7)) 
print("Binary Search (4):", binary_search(arr, 4))   
