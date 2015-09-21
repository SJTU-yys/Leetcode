# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 23:58:05 2015

@author: yys
"""

def lengthOfLongestSubstring(s):
    char_dict = {}
    start = 0
    res = 0
    for i,c in enumerate(s):
        if c in char_dict:
            res = max(res, i-start)
            start = max(start, char_dict[c]+1)
        char_dict[c] = i
    return max(res, len(s)-start)
    
print lengthOfLongestSubstring("abcabcbb")