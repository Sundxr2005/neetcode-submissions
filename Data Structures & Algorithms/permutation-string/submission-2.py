class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        freq1 = {}
        freq = {}

        # Frequency of s1
        for ch in s1:
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1

        l = 0
        r = 0

        while r < len(s2):

            # Add current character
            if s2[r] in freq:
                freq[s2[r]] += 1
            else:
                freq[s2[r]] = 1

            # If window becomes bigger than s1
            if r - l + 1 > len(s1):
                freq[s2[l]] -= 1

                if freq[s2[l]] == 0:
                    del freq[s2[l]]

                l += 1

            # Check if current window is a permutation
            if freq == freq1:
                return True

            r += 1

        return False