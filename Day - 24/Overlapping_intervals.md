# Problem Statement

Given an array of intervals `arr[][]`, where each interval is represented as `[start, end]`, the task is to merge all overlapping intervals.  
Two intervals `[a, b]` and `[c, d]` overlap if `a ≤ d` and `c ≤ b`.

### Examples

#### Example 1:
**Input:**  
`arr[][] = [[1,3],[2,4],[6,8],[9,10]]`

**Output:**  
`[[1,4], [6,8], [9,10]]`

**Explanation:**  
The intervals `[1,3]` and `[2,4]` overlap and can be merged into `[1,4]`. The other intervals `[6,8]` and `[9,10]` are non-overlapping.

---

# Approach

To merge overlapping intervals efficiently, we follow these steps:

### Steps:

1. **Sort Intervals by Start Time:**
   - Sort all intervals based on their start time. This ensures we can check overlapping intervals sequentially.

2. **Iterate and Merge:**
   - Initialize an empty list `merged` to store the merged intervals.
   - Add the first interval from the sorted list to `merged`.
   - Iterate through the rest of the intervals:
     - If the current interval overlaps with the last interval in `merged`, merge them by updating the end time.
     - Otherwise, add the current interval to `merged`.

3. **Return the Merged Intervals:**
   - After processing all intervals, the `merged` list will contain the merged intervals.

### Complexity:
- **Time Complexity:**  
  \(O(n \log n)\): Sorting the intervals takes \(O(n \log n)\), and iterating through the intervals takes \(O(n)\).  
- **Space Complexity:**  
  \(O(n)\): Result array `merged` can store up to all intervals in the worst case.

---
