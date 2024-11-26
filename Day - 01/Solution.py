from math import inf
class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        if n< 2 :
            return -1
        
        first = sec = float(-inf)
        for num in arr:
            if num > first:
                sec = first 
                first =num
            elif num > sec and num!= first:
                sec = num
        
        if sec == float(-inf):
            return -1
        else:
            return sec