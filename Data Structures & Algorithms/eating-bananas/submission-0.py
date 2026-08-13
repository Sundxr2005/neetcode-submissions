class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        front = 1 
        rear = max(piles)
        new = []
        while front <= rear:
            k = (front + rear) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                rear = k - 1 
                new.append(k)
            else:
                front = k + 1
        return min(new)

        