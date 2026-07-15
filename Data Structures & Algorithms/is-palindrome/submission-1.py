class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(c.lower() for c in s if c.isalnum())
        front = 0
        end = len(s1) - 1
        while front < end:
            if s1[front] != s1[end]:
                return False
            front += 1
            end -= 1
        return True