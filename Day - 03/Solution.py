class Solution:
    def reverseArray(self, arr):
        # code here
        n = len(arr)
        
        # apply a for loop till between of the for loop and start swapping them
        for i in range (n//2) :
            arr[i] , arr[n-i-1] = arr[n-i-1] , arr[i]
            
        return arr
        
        