def sort_integer_array(arr):
    """
    Sorts an array of integers in ascending order.

    :param arr: List of integers
    :return: Sorted list of integers
    """
    return sorted(arr)

# Example usage
if __name__ == "__main__":
    sample_array = [5, 3, 8, 1, 2]
    sorted_array = sort_integer_array(sample_array)
    print("Sorted Array:", sorted_array)