class Solution:
    def nextPermutation(self, arr):
      
        n = len(arr)
        
        # Step 1: Find the pivot
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        
        if i >= 0:  # If a valid pivot is found
            # Step 2: Find the next larger element to swap
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            # Step 3: Swap the elements at i and j
            arr[i], arr[j] = arr[j], arr[i]
        
        # Step 4: Reverse the suffix
        arr[i + 1:] = reversed(arr[i + 1:])


        # code here