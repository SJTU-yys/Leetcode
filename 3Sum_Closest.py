# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:30:34 2015

@author: yys
"""

def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    import sys
    nums = sorted(nums)
    res = nums[-1]+nums[-2]+nums[-3]
    diff = 0xFFFFFFFF
    i = 0
    l = len(nums)
    while i < l-2:
        j = l - 1
        k = i + 1
        while j > k:
            temp = nums[i]+nums[k]+nums[j]
            if temp == target:
                return temp
            elif temp < target:
                if diff > target - temp:
                    diff = target -temp
                    res = temp
                # Skip duplicate num[j-1]
                k += 1
                while j > k+1 and nums[k] == nums[k-1]:   k += 1
            else:
                if diff > temp - target :
                    diff = temp - target
                    res = temp
                j -= 1
                while nums[j] == nums[j+1] and j > k + 1:
                    j -= 1
        i += 1
        while nums[i] == nums[i-1] and i < l-1:
            i += 1
    return res