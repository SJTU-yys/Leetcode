# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:25:42 2015

@author: yys
"""

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    i = 0
    l = len(s)
    if numRows == 1:
        return s
    if l <= numRows:
        return s
    res = ""
    interval = 2*numRows - 2
    for j in range(numRows):
        i = j
        sub = interval - 2*j
        while i < l:
            res+=s[i]
            if j > 0 and j < numRows-1:
                if i+sub < l :
                    res+=s[i+sub]
            i+=interval
    return res
    
s = "PAYPALISHIRING"
print convert(s,3)