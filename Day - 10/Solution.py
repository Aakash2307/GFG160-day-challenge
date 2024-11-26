class Solution:
    ## Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        ## Your code here
        max_so_far = float('-inf')  # Initialize to a very small number
        max_ending_here = 0

        for num in arr:
            max_ending_here += num
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0

        return max_so_far
