class Solution:
    def mergeOverlap(self, intervals):
        if not intervals:
            return []

        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        # Step 2: Iterate through intervals and merge them
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                # Overlapping intervals, merge them
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                # Non-overlapping interval, add to result
                merged.append(intervals[i])

        return merged


# Example usage:
solution = Solution()
intervals = [[1, 3], [2, 4], [6, 8], [9, 10]]
print(solution.mergeOverlap(intervals))  # Output: [[1, 4], [6, 8], [9, 10]]
