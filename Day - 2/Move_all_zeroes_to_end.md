# Push All Zeros to the Right End of an Array

## Problem Statement
Given an array `arr[]`, move all zeros in the array to the right end while maintaining the order of the non-zero elements. Perform the operation **in place**.

---

## Examples

### Example 1:
**Input**:  
`arr = [1, 2, 0, 4, 3, 0, 5, 0]`  

**Output**:  
`[1, 2, 4, 3, 5, 0, 0, 0]`  

**Explanation**:  
The three `0`s are moved to the end while maintaining the order of non-zero elements.

---

### Example 2:
**Input**:  
`arr = [10, 20, 30]`  

**Output**:  
`[10, 20, 30]`  

**Explanation**:  
The array remains unchanged as there are no zeros.

---

## Approach

To solve this problem, we will use a **two-step process** with a temporary array to rearrange the elements.

---

### Steps

1. **Create a Temporary Array**:
   - Create a temporary array `temp` of the same size as the input array `arr[]`.

2. **Fill Non-Zero Elements**:
   - Traverse the input array using a loop.
   - For every non-zero element, add it to the `temp` array.

3. **Fill Remaining Zeros**:
   - After adding all non-zero elements, fill the remaining positions in the `temp` array with zeros.

4. **Replace Original Array**:
   - Copy the elements from the `temp` array back to the original array `arr[]`.

---

## Algorithm

### 1. Input and Initialization
- Take the input array `arr[]` of size `n`.
- Create a temporary array `temp[]` of size `n`.

### 2. First Loop:
- Traverse `arr[]` and add all non-zero elements to `temp[]`.

### 3. Second Loop:
- Add zeros to the remaining positions of `temp[]`.

### 4. Copy Back:
- Replace `arr[]` with the elements of `temp[]`.

---

## Complexity Analysis

- **Time Complexity**:  
  `O(n)` — Two loops through the array of size `n`.

- **Space Complexity**:  
  `O(n)` — Temporary array of size `n`.

---

## Implementation

```python
def push_zeros_to_end(arr):
    n = len(arr)
    temp = [0] * n  # Create a temporary array of size n
    j = 0  # Index for the temp array

    # First pass: Add non-zero elements to temp
    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1

    # Second pass: Add zeros to temp
    while j < n:
        temp[j] = 0
        j += 1

    # Replace original array with temp array
    for i in range(n):
        arr[i] = temp[i]

    return arr
