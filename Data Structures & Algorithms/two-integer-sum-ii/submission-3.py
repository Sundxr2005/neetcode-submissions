class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        rear = len(numbers) -1
        while numbers[front] + numbers[rear] != target:
            if numbers[front] + numbers[rear] > target:
                rear -= 1
            if numbers[front] + numbers[rear] < target:
                front += 1
        return [front + 1, rear + 1]