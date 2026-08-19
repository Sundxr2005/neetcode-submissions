class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxx = 0
        freq = {}

        while r < len(s):

            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1

            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1

            maxx = max(maxx, r - l + 1)

            r += 1

        return maxx