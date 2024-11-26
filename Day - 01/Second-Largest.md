# Find the Second Largest Element in an Array

## Problem Statement
Given an array of positive integers `arr[]`, return the **second largest element** in the array. If the second largest element doesn't exist, return `-1`.

### Constraints:
- **Array Size**: `2 ≤ arr.size() ≤ 10^5`
- **Element Range**: `1 ≤ arr[i] ≤ 10^5`

---

## Examples

### Example 1:
**Input**:  
`arr = [12, 35, 1, 10, 34, 1]`  

**Output**:  
`34`  

**Explanation**:  
The largest element is `35` and the second largest is `34`.

---

### Example 2:
**Input**:  
`arr = [10, 5, 10]`  

**Output**:  
`5`  

**Explanation**:  
The largest element is `10`, and the second largest is `5`.

---

### Example 3:
**Input**:  
`arr = [10, 10, 10]`  

**Output**:  
`-1`  

**Explanation**:  
The largest element is `10`, but a second largest element does not exist as all elements are the same.

---

## Approach

This problem can be solved in a single pass through the array, maintaining two variables to track the **largest** and **second largest** elements.

### Steps:
1. **Initial Setup**:
   - Use two variables `first` and `sec` to store the largest and second largest numbers, respectively.
   - Initialize both `first` and `sec` to negative infinity (`float('-inf')`).

2. **Handle Edge Case**:
   - If the array length is less than `2`, return `-1` as no second largest element can exist.

3. **Iterate Through the Array**:
   - For each element `num` in the array:
     - **Case 1**: If `num > first`, update:
       - `sec = first` (the current largest becomes the second largest).
       - `first = num` (update the largest).
     - **Case 2**: If `num < first` but `num > sec`:
       - Update `sec = num` (the current number becomes the second largest).
     - **Skip Equal Values**: If `num == first`, do nothing.

4. **Final Check**:
   - After the loop, if `sec` is still negative infinity (`float('-inf')`), it means no valid second largest element was found, so return `-1`.
   - Otherwise, return `sec`.

---


