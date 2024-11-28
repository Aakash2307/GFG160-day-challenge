def circularSubarraySum(self, arr):
        n = len(arr)

        # Helper function: Standard Kadane's algorithm
        def kadane(nums):
            max_ending_here = max_so_far = nums[0]
            for num in nums[1:]:
                max_ending_here = max(num, max_ending_here + num)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far

        # Find the total sum of the array
        total_sum = sum(arr)

        # Case 1: Maximum subarray sum using Kadane's algorithm
        max_kadane = kadane(arr)

        # Case 2: Find minimum subarray sum to calculate circular sum
        # Invert array elements to use Kadane's for minimum sum
        inverted_arr = [-num for num in arr]
        min_sum = -kadane(inverted_arr)

        # Handle edge case: All elements are negative
        if min_sum == total_sum:
            return max_kadane

        # Return the maximum of the two cases
        return max(max_kadane, total_sum - min_sum)