"""
Problem: Valid Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Difficulty: Easy
Pattern: String, Sorting, HashMap

Time Complexity: O(n+m)
Space Complexity: O(1)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT={},{}
        if len(s)!= len(t):
            return False
        for i in range(len(s)):
            countS[s[i]]= 1+countS.get(s[i],0)
            countT[t[i]]= 1+countT.get(t[i],0)

        for c in countS:
            if countS[c]!= countT.get(c,0):
                return False
        return True
