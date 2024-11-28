# Problem Statement

Given an integer array `arr[]` in a circular fashion, find the maximum subarray sum assuming the array is circular.  

- In a circular array, we can traverse from the end of the array back to the beginning.  
- The task is to compute the maximum possible sum of a subarray considering both standard and circular traversal.

### Example

#### Input:
`arr[] = [8, -8, 9, -9, 10, -11, 12]`

#### Output:
`22`

**Explanation:**  
Starting from the last element `12`, moving circularly, the subarray `[12, 8, -8, 9, -9, 10]` gives the maximum sum `22`.

---

# Approach

To solve the problem efficiently, we need to consider two possible cases:

### Case 1: Non-circular Subarray (Standard)
- Use Kadane’s algorithm to find the maximum subarray sum in the array as if it were a regular (non-circular) array.

### Case 2: Circular Subarray
- To handle the circular nature:
  1. Calculate the total sum of the array.
  2. Find the **minimum subarray sum** using a modified Kadane’s algorithm (by inverting the sign of the elements).
  3. Subtract the minimum subarray sum from the total sum to get the maximum sum considering circular traversal.

### Special Case: All Elements Are Negative
- If all elements in the array are negative, the circular sum would equal the total sum, which is invalid for the circular case. In such scenarios, the result is the non-circular subarray sum obtained from Kadane's algorithm.

### Steps
1. Use Kadane’s algorithm to compute the maximum subarray sum for the non-circular case.
2. Calculate the total sum of the array.
3. Compute the minimum subarray sum using Kadane's algorithm on the inverted array.
4. Compare the maximum of:
   - Non-circular maximum sum (from Kadane’s).
   - Circular maximum sum (`total_sum - min_sum`).
5. Handle the edge case where all elements are negative.

---
