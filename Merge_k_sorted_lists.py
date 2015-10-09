# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:49:27 2015

@author: yys
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """

    import heapq
    
    queue = [(l.val, l) for l in lists if l]
    heapq.heapify(queue)
    dummy = ListNode(-1)
    tail = dummy
    while queue:
        val, node = queue[0]
        if node.next:
            heapq.heapreplace(queue, (node.next.val, node.next))
        else:
            heapq.heappop(queue)
        tail.next = node
        tail = tail.next
    
    return dummy.next