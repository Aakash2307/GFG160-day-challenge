# Strings Rotations of Each Other

This repository contains a Python solution to check if one string is a rotated version of another string.

---

## Problem Statement

You are given two strings of equal lengths, `s1` and `s2`. The task is to determine whether `s2` is a rotated version of `s1`.

### Definition
- A **rotation** of a string involves moving characters from the start of the string to the end, while preserving their order.

---

## Examples

### Example 1
**Input**:  
`s1 = "abcd"`  
`s2 = "cdab"`

**Output**:  
`True`

**Explanation**:  
After two right rotations of `s1`, it becomes equal to `s2`:
1. `"abcd"` → `"dabc"`
2. `"dabc"` → `"cdab"`

### Example 2
**Input**:  
`s1 = "abc"`  
`s2 = "cab"`

**Output**:  
`True`

---

## Solution Approach

### Steps:

1. **Check Lengths**:
   - If the lengths of `s1` and `s2` are not equal, they cannot be rotations of each other. Return `False`.

2. **Concatenate `s1` with Itself**:
   - Create a new string `concat` by concatenating `s1` with itself: `concat = s1 + s1`.

3. **Check for Substring**:
   - If `s2` is a substring of `concat`, then `s2` is a rotated version of `s1`.

This approach works because rotating `s1` in any way results in a substring of `s1 + s1`.

---