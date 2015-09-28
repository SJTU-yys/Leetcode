# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 23:57:08 2015

@author: yys
"""

def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    # Get the length of the digit
    if x >= 0:
        return x == int(str(x)[::-1])
    else:
        return False