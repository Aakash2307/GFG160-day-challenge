def minimize_difference(arr, k):
    n = len(arr)
    if n == 1:
        return 0  # If there's only one tower, the difference is zero.

    # Sort the array
    arr.sort()

    # Initial difference
    initial_diff = arr[-1] - arr[0]

    # Initialize smallest and largest
    smallest = arr[0] + k
    largest = arr[-1] - k

    # Ensure smallest is smaller than largest
    if smallest > largest:
        smallest, largest = largest, smallest

    # Iterate through the array and calculate the minimum difference
    for i in range(1, n):
        # The current element can be either increased or decreased
        min_height = min(smallest, arr[i] - k)
        max_height = max(largest, arr[i - 1] + k)

        # Update the difference
        initial_diff = min(initial_diff, max_height - min_height)

    return initial_diff
