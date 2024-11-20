Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]

Explanation: There are three 0s that are moved to the end.
Input: arr[] = [10, 20, 30]

Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.


Approach 

## 1 . The First thing is we would create another array of same size n
## 2 . Now we apply a for loop to know if the array contain a non zero value then it will add it to the temp value
## 3 . We apply for loop for temp loop telling if you find any zero start adding them
## 4 . Now the temp array would be the same array as the old array
