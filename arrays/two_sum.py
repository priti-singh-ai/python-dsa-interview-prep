"""
Problem: Two Sum
Given an array of integers nums and an integer target,
return the indices i and j such that nums[i] + nums[j] == target and i != j.
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Difficulty: Easy
Pattern: HashMap

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashmap:
                return [hashmap[diff], i]

            hashmap[num] = i
