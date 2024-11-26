
# Maximum Profit from Stock Prices

## Problem Statement
Given an array `prices` where each element represents the stock price on a given day:
- You can buy on one day and sell on a later day.
- Your task is to find the **maximum profit** possible. If no profit is possible, return `0`.

---

## Approach

### 1. **Initialize Variables**
- **`min_price`**: Tracks the lowest price encountered so far. Initialize it to a very large value (`infinity`).
- **`max_profit`**: Stores the maximum profit calculated. Initialize it to `0`.

### 2. **Iterate Over Prices**
For each price in the array:
1. **Update `min_price`**:  
   Compare the current price with `min_price`. If the current price is smaller, update `min_price`.
2. **Calculate Profit**:  
   Compute the profit by subtracting `min_price` from the current price:  
   `profit = price - min_price`.
3. **Update `max_profit`**:  
   If the calculated profit is greater than `max_profit`, update `max_profit`.

### 3. **Return Result**
At the end of the loop, return `max_profit`. If no profit is possible, `max_profit` will remain `0`.

---

## Edge Cases
1. **Empty Array**: If the input array is empty, return `0`.
2. **Descending Prices**: If prices are in descending order, no profit can be made. Return `0`.
3. **Single Price**: If there’s only one price, return `0` as selling is not possible.

---

## Pseudocode
---

## Complexity Analysis
- **Time Complexity**:  
  `O(n)` — We iterate through the array once.
- **Space Complexity**:  
  `O(1)` — Only constant space is used for variables.

---

## Example Walkthrough

### Input:
`prices = [61, 44, 70, 78, 73, 95, 27, 1]`

### Execution:
1. Initialize `min_price = inf`, `max_profit = 0`.
2. Traverse the array:
   - Day 1 (price = 61):  
     `min_price = 61`, `max_profit = 0`
   - Day 2 (price = 44):  
     `min_price = 44`, `max_profit = 0`
   - Day 3 (price = 70):  
     `profit = 70 - 44 = 26`, `max_profit = 26`
   - Day 4 (price = 78):  
     `profit = 78 - 44 = 34`, `max_profit = 34`
   - Day 5 (price = 73):  
     `profit = 73 - 44 = 29`, `max_profit = 34`
   - Day 6 (price = 95):  
     `profit = 95 - 44 = 51`, `max_profit = 51`
   - Day 7 (price = 27):  
     `min_price = 27`, `profit = 27 - 27 = 0`, `max_profit = 51`
   - Day 8 (price = 1):  
     `min_price = 1`, `profit = 1 - 1 = 0`, `max_profit = 51`

### Output:
`max_profit = 51` (Buy at `44` and sell at `95`).

---

## Key Points
- The approach ensures you always "buy" at the lowest price before the current day.
- It calculates valid profits only when "selling" occurs after "buying."

