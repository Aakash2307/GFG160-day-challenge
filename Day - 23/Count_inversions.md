# Problem Statement

Given an array of integers `arr[]`, find the **Inversion Count**.  
An inversion occurs when two elements `arr[i]` and `arr[j]` satisfy the conditions:
1. `arr[i] > arr[j]`  
2. `i < j`  

### Inversion Count:
- If the array is already sorted, the inversion count is `0`.  
- If the array is sorted in reverse order, the inversion count is maximum.

### Examples

#### Example 1:
**Input:**  
`arr[] = [2, 4, 1, 3, 5]`  

**Output:**  
`3`  

**Explanation:**  
The array `[2, 4, 1, 3, 5]` has three inversions:  
- `(2, 1)`  
- `(4, 1)`  
- `(4, 3)`  

---

# Approach

To count inversions efficiently, we use the **Merge Sort** algorithm. This approach leverages the divide-and-conquer strategy to count inversions while sorting the array.

### Steps:

1. **Divide the Array:**
   - Recursively divide the array into two halves until each subarray contains a single element.

2. **Merge and Count:**
   - While merging two sorted halves, count the number of inversions:
     - If `arr[i] > arr[j]`, then all elements after `i` in the left half are also greater than `arr[j]`.  
       This is because the two halves are sorted.

3. **Combine Results:**
   - The total inversion count is the sum of:
     - Inversions in the left half.
     - Inversions in the right half.
     - Split inversions (between the two halves).

### Complexity:
- **Time Complexity:**  
  \(O(n \log n)\): The array is divided \(O(\log n)\) times, and merging takes \(O(n)\) time.  
- **Space Complexity:**  
  \(O(n)\): Temporary arrays are used during merging.

---

