class Solution:
    # Function to merge two sorted halves and count inversions
    def mergeAndCount(self, arr, left, mid, right):
        temp = []
        i, j = left, mid + 1
        invCount = 0

        # Merge the two halves while counting inversions
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                # Count inversions
                temp.append(arr[j])
                invCount += (mid - i + 1)  # Remaining elements in left half are inversions
                j += 1

        # Copy remaining elements from left half
        while i <= mid:
            temp.append(arr[i])
            i += 1

        # Copy remaining elements from right half
        while j <= right:
            temp.append(arr[j])
            j += 1

        # Copy sorted elements back into the original array
        for idx, val in enumerate(temp):
            arr[left + idx] = val

        return invCount

    # Function to perform merge sort and count inversions
    def mergeSortAndCount(self, arr, left, right):
        if left >= right:
            return 0

        mid = left + (right - left) // 2
        invCount = 0

        # Count inversions in left half
        invCount += self.mergeSortAndCount(arr, left, mid)

        # Count inversions in right half
        invCount += self.mergeSortAndCount(arr, mid + 1, right)

        # Count split inversions
        invCount += self.mergeAndCount(arr, left, mid, right)

        return invCount

    # Main function to find inversion count
    def inversionCount(self, arr):
        return self.mergeSortAndCount(arr, 0, len(arr) - 1)


# Example usage:
solution = Solution()
arr = [2, 4, 1, 3, 5]
print(solution.inversionCount(arr))  # Output: 3
