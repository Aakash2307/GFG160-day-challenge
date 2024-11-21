class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
       
        n = len(arr)
        freq = {}
        res = []
    
        # find frequency of each number
        for ele in arr:
            freq[ele] = freq.get(ele, 0) + 1
    
        # Iterate over each key-value pair in the hash map
        for ele, cnt in freq.items():
            
            # Add the element to the result, if its frequency
            # is greater than floor(n/3)
            if cnt > n // 3:
                res.append(ele)
    
        if len(res) == 2 and res[0] > res[1]:
            res[0], res[1] = res[1], res[0]
        return res
