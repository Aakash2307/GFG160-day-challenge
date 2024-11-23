# Maximum Profit from Stock Prices

## Problem Statement

You are given an array `price[]` where each element represents the cost of a stock on a specific day. You may decide to buy or sell the stock on any day, but you can only sell a stock after buying it. Multiple stocks cannot be held simultaneously. Your task is to calculate the **maximum profit** you can achieve.

---

## Example

### Example 1:
**Input:**  
`price[] = [100, 180, 260, 310, 40, 535, 695]`  
**Output:**  
`865`  

**Explanation:**  
1. Buy the stock on day 0 at price `100` and sell it on day 3 at price `310`:  
   Profit = `310 - 100 = 210`.
2. Buy the stock on day 4 at price `40` and sell it on day 6 at price `695`:  
   Profit = `695 - 40 = 655`.  
   
**Maximum Profit:** `210 + 655 = 865`.

---

## Approach

### Steps to Solve:
1. **Initialize a Variable `profit`:**  
   Set `profit` to `0` to keep track of the total profit.

2. **Iterate Through the Prices Array:**  
   - Start from the second day (index `1`) and compare each day’s price with the previous day’s price.
   - If `price[i] > price[i-1]`, calculate the difference (`price[i] - price[i-1]`) and add it to `profit`.

3. **Return the Total Profit:**  
   The accumulated `profit` will give the maximum possible profit.

### Key Idea:
- You are adding the positive difference between consecutive days whenever the price increases. This approach effectively identifies all potential profits from each upward trend in prices.

---





