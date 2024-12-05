class Solution:
    
    # Function to check whether two strings are anagrams of each other
    def areAnagrams(self, s1, s2):
        # If lengths of the strings are not the same, they can't be anagrams
        if len(s1) != len(s2):
            return False
        
        # Import Counter from collections to count the characters
        from collections import Counter
        
        # Count the frequency of characters in both strings
        c1 = Counter(s1)
        c2 = Counter(s2)
        
        # Compare the frequency dictionaries
        return c1 == c2