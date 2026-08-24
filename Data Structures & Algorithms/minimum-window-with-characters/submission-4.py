class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0
        r = 0

        tfreq = {}
        sfreq = {}

        # Frequency of characters required from t
        for i in t:
            if i in tfreq:
                tfreq[i] += 1
            else:
                tfreq[i] = 1

        # Number of different characters we need
        need = len(tfreq)

        # Number of different characters currently satisfied
        have = 0

        minn = float("inf")
        ans = ""

        while r < len(s):

            # Add s[r] to current window
            if s[r] in sfreq:
                sfreq[s[r]] += 1
            else:
                sfreq[s[r]] = 1

            # Character has just reached its required frequency
            if s[r] in tfreq and sfreq[s[r]] == tfreq[s[r]]:
                have += 1

            # Current window contains everything we need
            while have == need:

                # Save smallest valid window
                if r - l + 1 < minn:
                    minn = r - l + 1
                    ans = s[l:r + 1]

                # Remove s[l]
                sfreq[s[l]] -= 1

                # Removing it made the requirement unsatisfied
                if s[l] in tfreq and sfreq[s[l]] < tfreq[s[l]]:
                    have -= 1

                l += 1

            r += 1

        return ans