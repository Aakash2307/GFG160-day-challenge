# Maximum Sum of a Subarray

### Problem Statement:
Given an integer array `arr[]`, your task is to find the **maximum sum** of a contiguous subarray. A subarray is a contiguous part of the array, and the maximum sum is the largest sum that can be obtained from any subarray within the given array.

#### Examples:
**Input:**  
`arr[] = [2, 3, -8, 7, -1, 2, 3]`  
**Output:**  
`11`  

**Explanation:**  
The subarray `{7, -1, 2, 3}` has the largest sum, which is `11`.

---

### Approach:
We use **Kadane's Algorithm**, a well-known dynamic programming technique, to solve this problem in linear time (`O(n)`). Here's a step-by-step explanation of the approach implemented in the code:

1. **Initialization**:
   - Use a variable `max_so_far` to keep track of the maximum sum encountered so far. Initialize it to negative infinity (`-inf`) to ensure it can handle arrays with all negative numbers.
   - Use another variable `max_ending_here` to track the maximum sum of the subarray ending at the current position.

2. **Iterate Through the Array**:
   - Add the current element to `max_ending_here`.
   - Update `max_so_far` if `max_ending_here` is greater than `max_so_far`.
   - If `max_ending_here` becomes negative, reset it to `0`. This is because a negative sum will not contribute positively to any subarray, so we start a new subarray.

3. **Return the Result**:
   - At the end of the loop, `max_so_far` will contain the maximum sum of any subarray in the array.

---
