# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:25:26 2015

@author: yys
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(val)
            else:
                i += 1
        return len(nums)