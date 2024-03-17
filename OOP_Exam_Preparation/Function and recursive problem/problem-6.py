#Write a Python function to count the occurrences of a specific element in a list recursively.
def count_occurrences(arr, target):
    if not arr:
        return 0
    return (arr[0] == target) + count_occurrences(arr[1:], target)

my_list = [1, 2, 3, 4, 2, 2, 5, 6, 2]
target_element = 2
print("Target element in the list : ", count_occurrences(my_list, target_element))
