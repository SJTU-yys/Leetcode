# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 10:50:05 2015

@author: yys
"""

def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if len(nums) < 4:
        return []
    nums = sorted(nums)
    res = []
    length = len(nums)
    if length == 0:
        return res
    
    map = {}
    for i in range(length-3):
        for j in range(i+1,length-2):
            # Given the first two numbers and find the last two
            pairs = twoSum(nums[j+1:], target-nums[i]-nums[j])
            if pairs and (nums[i],nums[j]) not in map:
                    map[(nums[i],nums[j])] = pairs
                    for pair in pairs:
                        res.append([nums[i],nums[j],pair[0],pair[1]])
                    
    return res
    
def twoSum(num, target):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(num) == []:
        return []
    
    res = set()
    _map = {}
    for i in range(len(num)):
        if num[i] not in _map:
            _map[target-num[i]] = i
        else: 
            res.add((num[_map[num[i]]],num[i]))
    return res
    
S = [-5, -4, -3, -2, 1, 3, 3, 5]
print fourSum(S, -11)