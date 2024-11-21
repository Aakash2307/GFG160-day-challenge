from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        n = len(prices)
        
        # to know the count of the difference of the maximum and minimum
        res =0

        
        # A for loop to run i through the whole array and subtracting numbers from its previous value where the condition is the number should be bigger than 
        # its previous value 
        for i in range(1 , n) :
            if prices[i] > prices[i-1]:
                res += (prices[i] - prices[i-1])
                
        return res
       