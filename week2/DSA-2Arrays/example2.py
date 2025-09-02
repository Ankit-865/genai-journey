# 1 Find the Largest Element in an Array
def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

print(find_largest([10, 4, 3, 50, 23, 90]))  

# Check if Array is Sorted (Ascending Order)
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

print(is_sorted([1, 2, 3, 4, 5]))  
print(is_sorted([5, 1, 2, 3]))     

# Move All Zeros to the End

def move_zeros(arr):
    result = [num for num in arr if num!=0]
    zeros =[0]* (len(arr) - len(result))
    return result + zeros
print (move_zeros([0,1,0,3,12,0,12]))
