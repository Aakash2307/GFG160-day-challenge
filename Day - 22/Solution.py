class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        # Sort citations in descending order
        citations.sort(reverse=True)
        
        h_index = 0
        
        # Iterate through the sorted array
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h_index = i + 1
            else:
                break
        
        return h_index


