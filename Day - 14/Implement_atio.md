# Implement Atoi

## Problem Statement
The goal is to convert a given string `s` into an integer without using any built-in conversion functions like `int()`. The conversion should follow these steps:

1. Skip any leading whitespaces in the string.
2. Identify if the number has a sign (`+` or `-`); if no sign is present, assume the number is positive.
3. Process the numeric portion of the string digit by digit until a non-digit character is encountered or the string ends. Ignore any leading zeros.
4. If no digits are present, return `0`.
5. Ensure that the result does not overflow:
   - Return \( 2^{31} - 1 \) if the result exceeds this value for positive numbers.
   - Return \( -2^{31} \) if the result is less than this value for negative numbers.

---

## Approach

### Steps:
1. **Initialization:**
   - Set the default `sign` to `1` (positive).
   - Initialize `res` to `0` to store the result.
   - Use an index `idx` to traverse the string.

2. **Skip Leading Whitespaces:**
   - Increment `idx` to bypass spaces until a non-whitespace character is found.

3. **Handle the Sign:**
   - If a `+` or `-` is encountered, update the `sign` accordingly and increment the index.

4. **Construct the Integer:**
   - Iterate through the characters while they are digits (`0` to `9`).
   - Convert each character to its integer equivalent and append it to `res` by multiplying the current `res` by 10 and adding the digit.
   - Check for overflow or underflow during the construction:
     - If `res` exceeds \( 2^{31} - 1 \), return the appropriate boundary value based on the sign.

5. **Return the Result:**
   - Multiply `res` by `sign` to account for the correct sign and return it.

---

