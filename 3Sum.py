# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:24:54 2015

@author: yys
"""

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = sorted(nums)
    res = []
    i = 0
    l = len(nums)
    if l == 0:
        return res
    while nums[i] <= 0 and i < l-1:
        # i denotes start and j denotes end, move k from i to j
        j = l-1
        while nums[j] >= 0 and j > 0:
            n = -(nums[i]+nums[j])
            for k in xrange(i+1,j):
                if nums[k] == n and [nums[i],nums[k],nums[j]] not in res:
                    res.append([nums[i],nums[k],nums[j]])
                    break
            j -= 1
            while nums[j] == nums[j+1] and j > 0:
                j -= 1
        i += 1
        while nums[i] == nums[i-1] and i < l-1:
            i += 1
    return res