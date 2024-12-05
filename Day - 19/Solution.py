class Solution:
    def minChar(self, s):
        # Helper function to compute the Longest Prefix Suffix (LPS) array
        def compute_lps(concat):
            n = len(concat)
            lps = [0] * n
            length = 0
            i = 1
            while i < n:
                if concat[i] == concat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        # Reverse the input string
        rev_s = s[::-1]

        # Concatenate the string with its reverse, separated by a unique character
        concat = s + '#' + rev_s

        # Compute the LPS array for the concatenated string
        lps = compute_lps(concat)

        # Minimum characters to add = original string length - LPS of the last character
        return len(s) - lps[-1]