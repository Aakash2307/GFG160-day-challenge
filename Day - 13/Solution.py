class Solution:
    
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)

        # Step 1: Segregate positive and non-positive numbers
        j = 0
        for i in range(n):
            if arr[i] <= 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1

        # Step 2: Work only on the positive part of the array
        positive_part = arr[j:]

        # Mark the indices corresponding to the numbers in the positive part
        for i in range(len(positive_part)):
            val = abs(positive_part[i])
            if 1 <= val <= len(positive_part):
                positive_part[val - 1] = -abs(positive_part[val - 1])

        # Step 3: Find the first missing positive number
        for i in range(len(positive_part)):
            if positive_part[i] > 0:
                return i + 1

        # If all numbers from 1 to len(positive_part) are present
        return len(positive_part) + 1