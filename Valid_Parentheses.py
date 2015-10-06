# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 13:36:34 2015

@author: yys
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
            
        map = {')':'(','}':'{',']':'['}
        stack = []
        for i in range(len(s)):
            if s[i] in map.values():
                stack.append(s[i])
            elif s[i] in map.keys():
                if stack:
                    if stack[-1] == map[s[i]]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if not stack:
            return True
        return False