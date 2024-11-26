## Problem Statement

Given an array of integers `arr[]` representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

**Note:** A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

---

## Approach to Find the Next Permutation

To find the next permutation of a given array, we need to follow these steps:

### Steps:

1. **Identify the Pivot:**
   - Start by finding the largest index `i` such that `arr[i] < arr[i + 1]`. This point marks the position where we can increase the current permutation.
   - If no such index `i` is found (i.e., the array is in descending order), this means we are already at the last permutation, and we need to rearrange the array into the lowest possible order (ascending order).

2. **Find the Next Larger Element:**
   - If a valid pivot `i` is found, locate the largest index `j` such that `arr[j] > arr[i]` and `j > i`. This element will be the next larger element that we swap with `arr[i]` to get a greater permutation.

3. **Swap the Elements:**
   - Swap `arr[i]` and `arr[j]`. This ensures that we get the next lexicographically larger permutation.

4. **Reverse the Suffix:**
   - After the swap, the portion of the array from index `i + 1` to the end will be in descending order. To ensure the smallest possible arrangement for the remaining elements, we reverse the suffix from `i + 1` onwards.

5. **Final Result:**
   - The modified array will now represent the next permutation. If the array was already at its last permutation, it will be rearranged into the smallest possible order.

### Example Walkthrough:

#### Example 1:
**Input:**  
`arr = [2, 4, 1, 7, 5, 0]`

- **Step 1:** Identify pivot: The largest index `i` where `arr[i] < arr[i + 1]` is `i = 3` (since `arr[3] = 7` and `arr[4] = 5`).
- **Step 2:** Find the next larger element: The largest `j` such that `arr[j] > arr[i]` and `j > i` is `j = 4` (since `arr[4] = 5`).
- **Step 3:** Swap: Swap `arr[3]` and `arr[4]`, resulting in `[2, 4, 1, 5, 7, 0]`.
- **Step 4:** Reverse the suffix: Reverse the elements after index 3, resulting in `[2, 4, 5, 0, 1, 7]`.

**Output:**  
`[2, 4, 5, 0, 1, 7]`

#### Example 2:
**Input:**  
`arr = [3, 2, 1]`

- **Step 1:** Identify pivot: No valid pivot is found since the array is in descending order.
- **Step 2:** Since no pivot is found, rearrange the array into the lowest possible order (ascending order): `[1, 2, 3]`.

**Output:**  
`[1, 2, 3]`

---
