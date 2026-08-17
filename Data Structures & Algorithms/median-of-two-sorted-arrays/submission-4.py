class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l = 0
        r = len(nums1)

        total = len(nums1) + len(nums2)
        half = (total + 1) // 2

        while l <= r:
            m = (l + r) // 2
            n = half - m

            l1 = float('-inf') if m == 0 else nums1[m - 1]
            r1 = float('inf') if m == len(nums1) else nums1[m]

            l2 = float('-inf') if n == 0 else nums2[n - 1]
            r2 = float('inf') if n == len(nums2) else nums2[n]

            if l1 <= r2 and l2 <= r1:

                if total % 2 != 0:
                    return max(l1, l2)

                return (max(l1, l2) + min(r1, r2)) / 2

            elif l1 > r2:
                r = m - 1

            else:
                l = m + 1