class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0 
        freq = {}
        freq1 = {}
        for i in s1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        while r < len(s2):
            if s2[r] in freq1:
                freq1[s2[r]] += 1
            else:
                freq1[s2[r]] = 1
            if r - l + 1 > len(s1):
                freq1[s2[l]] -= 1
                if freq1[s2[l]] == 0:
                    del freq1[s2[l]]
                l += 1
            if freq == freq1:
                return True
            
            r += 1
        return False

        