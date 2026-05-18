"""
Problem: Given a string s, return true if it is a palindrome, otherwise return false.
Example 1:
Input: s = "Was it a car or a cat I saw?"

Output: true


Difficulty: Easy
Pattern: String, Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
  def isPalindrome(self, s:str) ->True:
    res= "".join(c.lower() for c in s if c.isalnum())
    if res[::-1]!=res[::1]:
      return False
    return True
