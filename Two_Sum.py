# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 21:18:58 2015

@author: yys
"""

def twoSum(num, target):
    if len(num) == []:
        return None
    
    _map = {}
    for i in range(len(num)):
        if num[i] not in _map:
            _map[target-num[i]] = num[i]
        else:
            return (_map[num[i]],num[i])
    return None
    
num = [3,2,4]
target = 6
print twoSum(num, target)