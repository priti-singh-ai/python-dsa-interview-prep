"""
Problem: Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
Example:
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Difficulty: Medium
Pattern: HashMap

Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #hashmap for grouping
        for s in strs:
            count = [0]*26 # a...z
            for c in s:
                count[ord(c)-ord("a")] +=1 # substracting letter from asciicode of a
            res[tuple(count)].append(s) # Correct: convert to tuple to avoid type error       
        return list(res.values())
