# Add Binary Strings

## Problem Statement
Given two binary strings `s1` and `s2`, find the resultant binary string after adding them. The binary strings consist of only `0`s and `1`s. Note that:
- The input strings may contain leading zeros.
- The output string should not have any leading zeros.

### Example:
#### Input:
`s1 = "1101", s2 = "111"`
#### Output:
`10100`

#### Explanation:

---

## Approach

To solve the problem, follow these steps:

1. Convert the binary strings `s1` and `s2` into their decimal equivalents using `int()` with base `2`.
2. Add the decimal equivalents to get the total sum.
3. Convert the resultant sum back to a binary string using `bin()` and strip the `0b` prefix.
4. Return the resultant binary string, ensuring no leading zeros in the output.

---

