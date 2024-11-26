# Problem: Minimize Height Difference of Towers

Given an array `arr[]` representing the heights of `N` towers and a positive integer `K`, you must perform exactly one of the following operations on each tower:

1. **Increase the height** of the tower by `K`.
2. **Decrease the height** of the tower by `K`.

Your task is to find the **minimum possible difference** between the heights of the shortest and tallest towers after modifying each tower.

### Notes:
- It is compulsory to either increase or decrease the height by `K` for each tower.
- The resultant array should not contain any negative integers.

### Examples:

#### Example 1:
**Input**:  
`k = 2, arr[] = {1, 5, 8, 10}`  

**Output**:  
`5`  

**Explanation**:  
The array can be modified as `{1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}`.  
The difference between the largest and smallest values is `8 - 3 = 5`.

#### Example 2:
**Input**:  
`k = 3, arr[] = {3, 9, 12, 16, 20}`  

**Output**:  
`11`  

**Explanation**:  
The array can be modified as `{3+k, 9+k, 12-k, 16-k, 20-k} = {6, 12, 9, 13, 17}`.  
The difference between the largest and smallest values is `17 - 6 = 11`.

---

# Approach to Solve

### Step-by-Step Solution:

1. **Sort the Array**:  
   Sorting the array allows systematic analysis of the range of heights from minimum to maximum.

2. **Initial Difference**:  
   Calculate the difference between the initial maximum and minimum heights:
   \[
   \text{Initial Difference} = \text{arr[-1]} - \text{arr[0]}
   \]

3. **Modify Heights**:  
   For each tower, you can either increase the height by `K` or decrease it by `K`.

4. **Track Potential New Heights**:  
   - After modifying the heights, calculate the **new minimum and maximum heights**:
     \[
     \text{Smallest Height} = \min(\text{arr[0]} + K, \text{arr[i]} - K)
     \]
     \[
     \text{Largest Height} = \max(\text{arr[i-1]} + K, \text{arr[-1]} - K)
     \]

5. **Iterate to Minimize Difference**:  
   For each tower, simulate both operations and calculate the potential difference between the modified maximum and minimum heights. Keep track of the smallest difference.

6. **Edge Cases**:  
   - Ensure no tower height becomes negative after modification.
   - Handle cases where \(K >\) the smallest height, as heights cannot be negative.

---

### Algorithm in Python:
```python
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
