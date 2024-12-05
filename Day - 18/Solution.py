class Solution:
    def search(self, pat, txt):
        # Initialize an empty list to store the indices of occurrences
        result = []
        
        # Get the length of the pattern and text
        pat_len = len(pat)
        txt_len = len(txt)
        
        # Loop through the text string to find occurrences of the pattern
        for i in range(txt_len - pat_len + 1):
            # Check if the substring from the current index matches the pattern
            if txt[i:i + pat_len] == pat:
                result.append(i)
        
        return result