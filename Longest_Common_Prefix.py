# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 00:40:31 2015

@author: yys
"""

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    length_list = [len(s) for s in strs]
    l = min(length_list)
    index = 0
    c = True
    for i in range(l):
        flag = strs[0][i]
        for s in strs:
            if flag != s[i]:
                return strs[0][:i]
        index += 1

    return strs[0][:index]