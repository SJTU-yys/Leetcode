# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 23:47:14 2015

@author: yys
"""

def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    # length == 0
    if str == "":
        return 0
    
    str = str.strip().split()[0]
    # length == 1
    if len(str) == 1: 
        if str.isdigit():
            return int(str)
        else:
            return 0
    
    # length > 1
    # check the start of the number
    i = 0
    if str[0] == '+' or str[0] == '-':
        if str[1].isdigit():
            start = i
        else:
            return 0
    elif str[0].isdigit():
        start = i
    else:
        return 0
    
    i = 0
    while i < len(str)-1:
        if str[i+1].isdigit():
            i+=1
        else:
            break
    end = i
    
    res = int(str[start:end+1])
    if res <= 0x7FFFFFFF and res >= -0x7FFFFFFF-1:
        return res
    elif res > 0x7FFFFFFF: 
        return 0x7FFFFFFF
    else:
        return -0x7FFFFFFF-1
        
print myAtoi('123ssda4')