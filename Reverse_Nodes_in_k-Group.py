# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:47:28 2015

@author: yys
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        while slow:
            fast = slow
            i = 0
            while fast and i < k:
                fast = fast.next
                i += 1
            if fast:
                tmp = slow.next
                for j in range(k-1):
                    p = tmp.next
                    tmp.next = p.next 
                    p.next = slow.next
                    slow.next = p
                slow = tmp
            else:
                return dummy.next
        