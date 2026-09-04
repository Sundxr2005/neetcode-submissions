class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        r = 0 
        freq = {}
        maxx = 0
        while r < len(s):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            wsize = (r - l) + 1
            maxdict = max(freq.values())
            if wsize - maxdict <= k:
                maxx = max(maxx, wsize)
            else:
                freq[s[l]] -= 1
                l += 1 
            r += 1
        return maxx
        