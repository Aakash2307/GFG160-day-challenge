# Problem Statement

Given an integer array `citations[]`, where `citations[i]` represents the number of citations a researcher received for the \(i\)th paper, find the **H-index**.  

### H-Index Definition:
The **H-index** is the largest number \(H\) such that the researcher has at least \(H\) papers with at least \(H\) citations each.

### Examples

#### Example 1:
**Input:**  
`citations[] = [3, 0, 5, 3, 0]`

**Output:**  
`3`

**Explanation:**  
There are at least 3 papers (3, 5, 3) with at least 3 citations each.

---

# Approach

To calculate the H-index efficiently, we can follow these steps:

### Steps:
1. **Sort the citations array in descending order.**  
   Papers with the most citations will be at the beginning.
2. **Iterate through the sorted array** and check if the citation count of the \(i\)th paper is greater than or equal to \(i + 1\):  
   - If true, update the H-index as \(i + 1\).
   - If false, break the loop since papers beyond this point will not satisfy the H-index condition.
3. **Return the H-index** as the result.

### Explanation:
By sorting in descending order, the condition for the H-index (`citations[i] >= i + 1`) can be checked sequentially. This ensures that the largest \(H\) satisfying the criteria is found.

### Complexity:
- **Time Complexity:**  
  - Sorting the array: \(O(n \log n)\)
  - Iterating through the array: \(O(n)\)  
  **Overall:** \(O(n \log n)\)
- **Space Complexity:**  
  \(O(1)\) for in-place computations.

---


