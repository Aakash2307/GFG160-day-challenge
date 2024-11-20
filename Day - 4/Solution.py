class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        
        d = d % len(arr)
        
        rotated = arr[d:] + arr[:d]
        
        for i in range(n):
            arr[i] = rotated[i]
            
        return arr

