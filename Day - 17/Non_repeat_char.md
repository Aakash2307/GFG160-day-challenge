# Find the First Non-Repeating Character

This repository contains a Python solution to find the first non-repeating character in a given string.

## Problem Statement

Given a string `s` consisting of lowercase Latin letters, the task is to find the first non-repeating character in the string. If there is no non-repeating character, return `'$'`.

### Note
- When the function returns `'$'`, the driver code will output `-1`.

---

### Examples

#### Example 1
**Input**:  
`s = "geeksforgeeks"`  

**Output**:  
`'f'`

**Explanation**:  
In the given string, `'f'` is the first character that does not repeat.

---

## Solution Approach

The solution involves the following steps:

1. **Frequency Count with Index Tracking**:  
   Use a dictionary to store the frequency of each character along with its first occurrence index.
   
   - Key: Character from the string.  
   - Value: A list containing frequency and index (`[frequency, index]`).

2. **Iterate Over the String**:  
   Count the frequency of each character while recording its first occurrence index.

3. **Find the Non-Repeating Character**:  
   Iterate through the dictionary to find the character with frequency `1` and the smallest index.

4. **Return Result**:  
   If a non-repeating character is found, return it. Otherwise, return `'$'`.

---