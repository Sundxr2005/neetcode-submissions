class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        ans = []
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        for num, count in freq.items():
            res.append((count, num))
        res.sort(reverse=True)
        for i in range(k):
            ans.append(res[i][1])
        return ans


