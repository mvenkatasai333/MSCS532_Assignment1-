# Insertion Sort Algorithm (Monotonically Decreasing Order)
def insertion_sort_desc(arr):
    """
    Sorts an array in monotonically decreasing order using insertion sort.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements that are smaller than key
        # to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr
if __name__ == "__main__":
    numbers = [12, 5, 8, 19, 3, 7]
    print("Original Array:", numbers)
    sorted_numbers = insertion_sort_desc(numbers)
    print("Sorted Array (Decreasing Order):", sorted_numbers)