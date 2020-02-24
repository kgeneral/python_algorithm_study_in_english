# https://leetcode.com/problems/merge-two-sorted-lists/submissions/
# elapsed time : 30 min

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        it1 = l1
        it2 = l2
        
        merged = ListNode(-1)
        itm = merged
        while it1 != None and it2 != None:
            if it1.val < it2.val:
                itm.next = it1
                itm = it1
                it1 = it1.next
            else:
                itm.next = it2
                itm = it2
                it2 = it2.next
            
        if it1 != None: 
            itm.next = it1
        else:
            itm.next = it2
            
        return merged.next
