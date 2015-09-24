# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 23:28:10 2015

@author: yys
"""

def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    # Convert the integer into a string 
    # Directly reverse the string
    t = str(abs(x))
    if x > 0:
        res = int(t[::-1])
    else:
        res = -int(t[::-1])
    if res < 0x7FFFFFFF and res > -0x7FFFFFFF-1:
        return res
    else:
        return 0