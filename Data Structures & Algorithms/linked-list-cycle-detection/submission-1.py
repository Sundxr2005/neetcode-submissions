# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        freq = {}
        while head:
            if head.val in freq:
                freq[head.val] += 1
            else:
                freq[head.val] = 1
            if freq[head.val] > 2:
                break
            head = head.next
        while head:
            if freq[head.val] == 1:
                head = head.next
            else:
                return True
        return False