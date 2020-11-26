# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummyHead = ListNode(0)
        output = dummyHead
        while(l1 or l2):
            if not l1:
                output.next = ListNode(l2.val)
                l2=l2.next 
            elif not l2:
                output.next = ListNode(l1.val)
                l1=l1.next 
            else:
                if l1.val<=l2.val:
                    output.next = ListNode(l1.val) 
                    l1=l1.next 
                else:
                    output.next = ListNode(l2.val) 
                    l2=l2.next 

            output = output.next 
        return dummyHead.next
                
        