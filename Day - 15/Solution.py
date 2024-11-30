
class Solution:
    def addBinary(self, s1, s2):
        # Step 1: Convert binary strings to decimal numbers
        n1 = int(s1, 2)
        n2 = int(s2, 2)
        
        # Step 2: Add the two decimal numbers
        tot = n1 + n2
        
        # Step 3: Convert the result back to binary and strip the prefix
        result = bin(tot)[2:]
        
        return result
