# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        left = 0
        right = len(string) - 1

        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        
        return True