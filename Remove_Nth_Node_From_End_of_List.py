# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:40:49 2015

@author: yys
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
            
        fast = head
        slow = head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        nex = slow.next
        
        i = 0
        while fast and i < n-1:
            fast = fast.next
            i += 1
        if not fast:
            return None
        
        # Find the previous node and the next node
        while fast.next:
            fast = fast.next
            prev = slow
            slow = slow.next
            nex = slow.next
        
        prev.next = nex
        return dummy.next