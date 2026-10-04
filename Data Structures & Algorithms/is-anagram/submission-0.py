class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = sorted(s)
        second = sorted(t)
        if len(first) == len(second):
            if first == second:
                return True
        return False