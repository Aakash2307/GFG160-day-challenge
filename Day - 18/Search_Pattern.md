# Find All Occurrences of a Pattern in a Text String

This repository contains a Python solution to find all the starting indices of occurrences of a given pattern string within a text string.

---

## Problem Statement

Given two strings:
- `txt` (the text string)
- `pat` (the pattern string)

The task is to find all the starting indices where the pattern appears in the text. The indices should be 0-based. If the pattern does not appear in the text, return an empty list.

---

### Examples

#### Example 1
**Input**:  
`txt = "abcab"`  
`pat = "ab"`

**Output**:  
`[0, 3]`

**Explanation**:  
The string `"ab"` occurs twice in the text string `txt`.  
- The first occurrence starts at index `0`.  
- The second occurrence starts at index `3`.

#### Example 2
**Input**:  
`txt = "abcdef"`  
`pat = "gh"`

**Output**:  
`[]`

**Explanation**:  
The pattern `"gh"` does not appear in the text string `"abcdef"`.  

---

## Solution Approach

The solution involves the following steps:

1. **Initialize an Empty Result List**:  
   Create an empty list to store the starting indices of the occurrences of the pattern in the text.

2. **Pattern and Text Lengths**:  
   Compute the lengths of the pattern (`pat_len`) and text (`txt_len`) to control the iteration.

3. **Sliding Window Search**:  
   Use a sliding window of size equal to the pattern's length to traverse the text string:
   - At each position `i`, extract the substring `txt[i:i+pat_len]`.
   - Compare it with the pattern. If they match, append the index `i` to the result list.

4. **Return the Result**:  
   Return the list of indices. If no match is found, the result list will remain empty.

---
