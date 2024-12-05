class Solution:
    
    # Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self, s):
        char_count = {}
    
        # Count the frequency of each character
        for i, char in enumerate(s):
            if char in char_count:
                char_count[char][0] += 1
            else:
                char_count[char] = [1, i]  # [frequency, index]
        
        # Find the first character with frequency 1
        min_index = float('inf')
        result = '$'
        for char, (freq, index) in char_count.items():
            if freq == 1 and index < min_index:
                min_index = index
                result = char
        
        return result