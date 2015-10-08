# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 12:42:57 2015

@author: yys
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(res, n, n, '')
        return res
        
    def dfs(self, res, i, j, s):
        # i denotes the number of '('s left
        # j denotes the number of ')'s left
        # return list of all possible parenthesis based on s
        if i == 0 and j == 0:
            res.append(s)
        else:
            if i > 0:
                self.dfs(res, i-1, j, s+'(')
            if i < j:
                self.dfs(res, i, j-1, s+')')