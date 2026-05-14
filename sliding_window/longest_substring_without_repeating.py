"""
Problem: Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Difficulty: Hard
Pattern: HashMap, Array, Union find

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums)
        longest=0

        for i in nums:
            if (i-1) not in numSet:
                length=0
                while(i+length) in numSet:
                    length+=1
                longest= max(length,longest)
        return longest
