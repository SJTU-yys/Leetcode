# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        start = dummy
        i = 0
        while start.next and start.next.next:
            # Swap the next two nodes from start
            tmp = start.next
            p = tmp.next
            start.next = p
            tmp.next = p.next
            p.next = tmp
            start = tmp

        return dummy.next
