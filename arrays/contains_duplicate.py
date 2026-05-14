"""
Problem: Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Difficulty: Easy
Pattern: Array,HashTable, Sorting

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1=set(list(nums))
        if len(set1)!= len(nums):
            return True
        return False
