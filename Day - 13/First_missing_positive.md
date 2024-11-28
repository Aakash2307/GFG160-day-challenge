# Problem Statement

You are given an integer array `arr[]`. Your task is to find the smallest positive number missing from the array.

- **Note:** Positive numbers start from 1. The array may include negative integers as well.

### Examples

#### Example 1
**Input:**  
`arr[] = [2, -3, 4, 1, 1, 7]`  

**Output:**  
`3`  

**Explanation:**  
The smallest positive missing number is `3`.

---

# Approach

The approach leverages efficient in-place operations and segregates the array into positive and non-positive numbers to simplify the problem. The steps are as follows:

### Step 1: Segregate Positive and Non-positive Numbers
- Iterate through the array to separate positive numbers from non-positive numbers.
- Use two pointers (`i` and `j`) to swap non-positive numbers (≤ 0) to the beginning of the array.
- After segregation, only the positive part of the array is considered for further operations.

### Step 2: Marking Indices for Positive Numbers
- Work with the positive portion of the array (`positive_part`).
- For each number in the positive part:
  - Use its absolute value as an index to mark that the number is present.
  - To mark, negate the value at the corresponding index (`val - 1`), ensuring it lies within the array bounds (`1 ≤ val ≤ len(positive_part)`).

### Step 3: Find the Missing Positive Number
- Traverse the marked positive part.
- The first index with a positive value indicates the smallest missing positive number (`index + 1`).

### Step 4: Return the Result
- If all numbers from `1` to `len(positive_part)` are present, return `len(positive_part) + 1`.

---

