"""
Problem: Top K frequents
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
Example:
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Difficulty: Medium
Pattern: HashMap, Array,Sorting

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n]= 1+count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for j in range(len(freq)-1,0,-1):
            for num in freq[j]:
                res.append(num)
                if len(res) == k:
                    return res
