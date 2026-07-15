class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        new = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            front = i + 1
            rear = len(nums) - 1
            target = -nums[i]
            while front < rear:
                current = nums[front] + nums[rear]
                if current == target:
                    new.append([nums[i], nums[front], nums[rear]])
                    front += 1
                    rear -= 1
                    while front < rear and nums[front] == nums[front - 1]:
                        front += 1
                    while front < rear and nums[rear] == nums[rear + 1]:
                        rear -= 1
                elif current < target:
                    front += 1
                else: 
                    rear -= 1
        return new 
                
         