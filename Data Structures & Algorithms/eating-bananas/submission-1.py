class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        front = 1 
        rear = max(piles)
        res = max(piles)
        while front <= rear:
            k = (front + rear) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                rear = k - 1 

            else:
                front = k + 1
        return res

        