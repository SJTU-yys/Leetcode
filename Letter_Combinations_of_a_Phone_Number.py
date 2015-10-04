# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 10:20:47 2015

@author: yys
"""

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if digits == "":
        return []
    dist = {}
    start = 0
    for i in range(2,10):
        if i == 7 or i == 9:
            interval = 4
        else:
            interval = 3
        dist[str(i)] = []
        for j in range(start,start+interval):
            dist[str(i)].append(chr(ord('a')+j))
        start += interval
        
    i = 0
    res = [[] for n in range(len(digits)+1)]
    res[0] = [""]
    while i < len(digits):
        for j in range(len(res[i])):
            for t in dist[digits[i]]:
               res[i+1].append(res[i][j] + t)
        i+=1
    return res[-1]
digits = '2345'
print letterCombinations(digits)