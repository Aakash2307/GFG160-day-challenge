# Problem Statement

Given an array `arr[]` containing only 0s, 1s, and 2s, sort the array in ascending order.

### Examples

#### Example 1:
**Input:**  
`arr[] = [0, 1, 2, 0, 1, 2]`  

**Output:**  
`[0, 0, 1, 1, 2, 2]`  

**Explanation:**  
0s, 1s, and 2s are segregated into ascending order.

---

# Approach

To solve this problem efficiently, we use the **Dutch National Flag Algorithm**. This algorithm sorts the array with a single traversal in \(O(n)\) time complexity.

### Steps:
1. Initialize three pointers:
   - `low` for the position of 0s.
   - `mid` for the current element under examination.
   - `high` for the position of 2s.
2. Start with:
   - `low = 0`
   - `mid = 0`
   - `high = len(arr) - 1`
3. Traverse the array while `mid <= high`:
   - If `arr[mid] == 0`:
     - Swap `arr[low]` and `arr[mid]`.
     - Increment both `low` and `mid`.
   - If `arr[mid] == 1`:
     - Just increment `mid`.
   - If `arr[mid] == 2`:
     - Swap `arr[mid]` and `arr[high]`.
     - Decrement `high`.
4. Continue the process until all elements are sorted.

### Time Complexity:
- \(O(n)\): The array is traversed only once.

### Space Complexity:
- \(O(1)\): Sorting is performed in-place without using extra space.
