You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format.

Examples:

Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.
Input: arr[] = [1, 2, 3, 4, 5]
Output: []
Explanation: no candidate occur more than n/3 times.



Approach

Solved using hashmaps

first make a list of the unique numbers that are occuring in the list

we need to make a dict for this which we try to insert the element which does not exist if exist then increase the count by 1

now make a note of the frequency of the elements 

Now check which element has been occured more then n/3 times and return the number in ascending format