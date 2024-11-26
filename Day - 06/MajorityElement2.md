# Majority Element (n/3)

## Problem Statement

You are given an array of integers `arr[]` where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes. If no candidate receives more than one-third of the total votes, return an empty array.

### Example

#### Example 1:
**Input:**  
`arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]`  
**Output:**  
`[5, 6]`  

**Explanation:**  
Candidates `5` and `6` occur more than `n/3` times.

---

#### Example 2:
**Input:**  
`arr[] = [1, 2, 3, 4, 5]`  
**Output:**  
`[]`  

**Explanation:**  
No candidate occurs more than `n/3` times.

---

## Approach

This problem can be solved efficiently using a **HashMap** to count the occurrences of each number. Here’s the step-by-step breakdown:

1. **Initialize a Frequency Map:**  
   Use a dictionary to store the frequency of each unique element in the array.  
   - If the element is not present in the dictionary, initialize it with a count of `1`.
   - If the element already exists, increment its count by `1`.

2. **Find Elements Occurring More Than `n/3` Times:**  
   Iterate through the frequency map and check if the frequency of any element is greater than `n/3`.

3. **Return the Result in Ascending Order:**  
   Collect all elements that satisfy the condition and sort them in ascending order before returning.

---


