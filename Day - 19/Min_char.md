# Minimum Characters to Add for Palindrome

This repository contains a Python solution to determine the minimum number of characters required to be added at the front of a string to make it a palindrome.

---

## Problem Statement

Given a string `s`, the task is to calculate the minimum characters that need to be added at the front of the string to make it a palindrome.  
A palindrome is a sequence of characters that reads the same backward as forward.

---

### Examples

#### Example 1
**Input**:  
`s = "abc"`

**Output**:  
`2`

**Explanation**:  
Add `'c'` and `'b'` to the front of the string to make it a palindrome: `"cbabc"`.

#### Example 2
**Input**:  
`s = "aacecaaaa"`

**Output**:  
`2`

**Explanation**:  
Add `'a'` and `'a'` to the front of the string to make it a palindrome: `"aaaacecaaaa"`.

---

## Solution Approach

To solve this problem efficiently, we use the **KMP Algorithm** to compute the **Longest Prefix Suffix (LPS)** array, which helps us determine the longest palindromic suffix of the given string. This allows us to calculate the minimum number of characters to be added.

### Steps:

1. **Reverse the Input String**:  
   Reverse the given string `s` to get `rev_s`.

2. **Concatenate Strings**:  
   Concatenate `s`, a special separator (`#`), and `rev_s` to form a new string:  
   `concat = s + '#' + rev_s`.

3. **Compute the LPS Array**:  
   Use the KMP algorithm to compute the **Longest Prefix Suffix (LPS)** array for the concatenated string.  
   The value of the last element in the LPS array represents the length of the longest palindromic suffix in the original string.

4. **Calculate the Result**:  
   The minimum characters to be added at the front is the difference between the length of the string and the length of the longest palindromic suffix:  
   `result = len(s) - lps[-1]`.

---