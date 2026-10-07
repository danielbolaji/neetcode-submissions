class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        copy = s[::-1]
        if copy == s:
            return True
        return False