# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:08:34 2015

@author: yys
"""

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    res = 0
    i = len(s)-1
    while i > 0:
        if dict[s[i-1]] >= dict[s[i]]:
            res += dict[s[i]]
            i -= 1
        else:
            res += dict[s[i]]-dict[s[i-1]]
            i -= 2
    if i == 0:
        res += dict[s[i]]
        
    return res
    
print romanToInt("DXL")