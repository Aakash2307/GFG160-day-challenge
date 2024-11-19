Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.


Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105


APPROACH

Initial Setup:

The method uses two variables, first and sec, to track the largest and second largest numbers in the list, respectively.
Both first and sec are initialized to negative infinity (float(-inf)), which is a way to ensure that any number in the array will be larger than these initial values during the first few iterations.
Handling Edge Case (Length Check):

First, the function checks if the length of the array is less than 2. If the array has fewer than two elements, it immediately returns -1 because there can be no second largest number.
Iterating Through the Array:

The core of the logic is a single pass (linear traversal) through the array:
For each number num in the array:
If num is greater than first (i.e., it is larger than the current largest number), then:
The current first becomes the new sec (second largest), and
num becomes the new first (largest).
If num is not greater than first, but is greater than sec and not equal to first, then:
Update sec to num (as num is now the second largest).
This ensures that, at the end of the loop, first holds the largest number and sec holds the second largest.
Final Check:

After the loop, the function checks if sec is still set to -inf. This would imply that a second largest number was not found (perhaps because the list had identical numbers or was too short). In this case, it returns -1.
If sec has been updated (i.e., there was a valid second largest number), it returns sec.