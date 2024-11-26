class Solution:

	# Function to find maximum
	# product subarray
    def maxProduct(self ,arr):
        n = len(arr)
        if n == 0:
            return 0
    
        # Initialize variables
        max_product = arr[0]
        current_max = arr[0]
        current_min = arr[0]
    
        # Iterate through the array
        for i in range(1, n):
            num = arr[i]
    
            # Since the number can be negative, we swap current_max and current_min
            if num < 0:
                current_max, current_min = current_min, current_max
    
            # Update current_max and current_min
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)
    
            # Update the overall maximum product
            max_product = max(max_product, current_max)
    
        return max_product
