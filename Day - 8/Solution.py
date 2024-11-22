class Solution:
   def maximumProfit(self, prices):
        if not prices:
            return 0
    
        # Initialize variables
        min_price = float('inf')  # To track the smallest price seen so far
        max_profit = 0            # To track the maximum profit
    
        # Iterate through prices
        for price in prices:
            # Update the minimum price
            min_price = min(min_price, price)
    
            # Calculate profit if we sell at the current price
            profit = price - min_price
    
            # Update the maximum profit
            max_profit = max(max_profit, profit)
    