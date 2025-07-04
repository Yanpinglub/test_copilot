def find_element(lst, target):
    """
    Find the index of the target element in the list.
    Returns -1 if the target is not found.
    """
    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1

# Example usage
my_list = [1, 2, 3, 4, 5]
target = 3
result = find_element(my_list, target)
print(f"Index of {target}: {result}")