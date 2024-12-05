# Check if Two Strings are Anagrams

This repository contains a Python solution to check whether two given strings are anagrams of each other. 

## Problem Statement

Two strings, `s1` and `s2`, consisting of lowercase alphabets, are given. The task is to determine if these strings are anagrams of each other. An anagram of a string is another string that contains the same characters, only the order of characters can be different.

### Examples

#### Example 1
**Input**:  
`s1 = "geeks"`  
`s2 = "kseeg"`  

**Output**:  
`true`

**Explanation**:  
Both strings have the same characters with the same frequency. Hence, they are anagrams.

---

## Solution Approach

The solution involves the following steps:

1. **Check Length**: If the lengths of `s1` and `s2` are different, they cannot be anagrams.
2. **Count Characters**: Use Python's `collections.Counter` to count the frequency of characters in both strings.
3. **Compare Frequencies**: Compare the frequency counts of both strings. If they match, the strings are anagrams; otherwise, they are not.

---