class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = [] 
        for i in nums1:
            res.append(i)
        for i in nums2:
            res.append(i)
        res.sort()
        l = 0
        r = len(res) - 1
        m = (l + r) // 2
        if len(res) % 2 != 0:
            return res[m]
        else:
            return (res[m] + res[m+1]) / 2


        