# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:50:02 2015

@author: yys
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
            
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                # Move j to the next one
                j += 1
            else:
                # If not equal, assign the (i+1)th element
                i += 1
                nums[i] = nums[j]
                j += 1
        return i+1