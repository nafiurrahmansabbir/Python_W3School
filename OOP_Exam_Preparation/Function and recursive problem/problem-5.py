#Write a Python function to perform binary search recursively on a sorted list
def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 11
index = binary_search_recursive(arr, target, 0, len(arr) - 1)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the list.")
