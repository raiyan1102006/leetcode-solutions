# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# Runtime: 60 ms, faster than 96.15% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.2 MB, less than 48.88% of Python3 online submissions for Add Two Numbers.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0
        while(l1 or l2 or carry):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum_ = x + y + carry
            current.next = ListNode(sum_%10)
            current = current.next
            carry = sum_ // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummyHead.next
            
            