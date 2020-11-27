# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Runtime: 28 ms, faster than 95.80% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.6 MB, less than 35.24% of Python3 online submissions for Reverse Linked List.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        currentNode = head
        prev = None
        while(1):
            tempNode = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = tempNode
            
            if not currentNode:
                break
            
        return(prev)