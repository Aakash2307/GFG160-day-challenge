# Approach to Rotate Array by `d` Elements in Counter-Clockwise Direction

### Problem Statement
Given an unsorted array `arr[]` and a positive integer `d`, you are tasked with rotating the array to the left (counter-clockwise direction) by `d` steps. The array should be modified in-place, and the rotation is considered circular.

### Explanation and Approach

To rotate the array to the left by `d` positions, we can approach the problem in the following way:

### Steps:

1. **Normalize the Number of Rotations**:
   - If `d` is greater than the length of the array `n`, rotating the array by `d` is equivalent to rotating it by `d % n` positions. This is because after every `n` rotations, the array returns to its original position. Hence, we first compute `d = d % n` to ensure we rotate the array by the effective number of steps.

2. **Split the Array into Two Parts**:
   - The array is split into two parts:
     - The first part consists of the elements from index `0` to `d-1` (i.e., `arr[0:d]`).
     - The second part consists of the elements from index `d` to `n-1` (i.e., `arr[d:n]`).

3. **Concatenate the Two Parts**:
   - To rotate the array to the left by `d` steps, we concatenate the second part (from `d` to `n-1`) with the first part (from `0` to `d-1`). This forms the rotated array.

4. **Copy the Rotated Array to the Original Array**:
   - After forming the rotated array, we copy its elements back to the original array `arr[]` in-place.

5. **Final Result**:
   - The original array `arr[]` is updated with the rotated values, and the array is returned as the output.

### Example Walkthrough:

#### Example 1:
**Input**:  
`arr[] = [1, 2, 3, 4, 5], d = 2`

1. Normalize `d`:  
   `d = 2 % 5 = 2`

2. Split the array into two parts:
   - First part: `arr[0:2] = [1, 2]`
   - Second part: `arr[2:5] = [3, 4, 5]`

3. Concatenate the parts:  
   The rotated array is `[3, 4, 5] + [1, 2] = [3, 4, 5, 1, 2]`

4. Copy the rotated array back to `arr`:  
   The array is now `[3, 4, 5, 1, 2]`

**Output**:  
`[3, 4, 5, 1, 2]`

---

#### Example 2:
**Input**:  
`arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3`

1. Normalize `d`:  
   `d = 3 % 10 = 3`

2. Split the array into two parts:
   - First part: `arr[0:3] = [2, 4, 6]`
   - Second part: `arr[3:10] = [8, 10, 12, 14, 16, 18, 20]`

3. Concatenate the parts:  
   The rotated array is `[8, 10, 12, 14, 16, 18, 20] + [2, 4, 6] = [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]`

4. Copy the rotated array back to `arr`:  
   The array is now `[8, 10, 12, 14, 16, 18, 20, 2, 4, 6]`

**Output**:  
`[8, 10, 12, 14, 16, 18, 20, 2, 4, 6]`

---

### Code Implementation:

```python
class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        
        # Normalize d to ensure it's within the array bounds
        d = d % len(arr)
        
        # Create a rotated array by concatenating two parts
        rotated = arr[d:] + arr[:d]
        
        # Copy the rotated array back to the original array
        for i in range(n):
            arr[i] = rotated[i]
            
        return arr
