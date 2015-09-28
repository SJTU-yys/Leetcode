# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:13:56 2015

@author: yys
"""

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    if s == "":
        if p == "":
            return True
                
    if p == "":
        if s == "":
            return True
        else:
            return False
            
    i = len(s)-1
    j = len(p)-1
    if str.isalpha(p[j]):
        if s == "":
            return False
        if s[i] == p[j]:
            return isMatch(s[:i],p[:j])
        else:
            return False
    if p[j] == '.':
        if s == "":
            return False
        return isMatch(s[:i],p[:j])
    if p[j] == '*':
        flag = p[j-1]
        # '.*' can match any string
        if flag == '.':
            res = False
            for i in range(len(s)+1):
                res = res or isMatch(s[:i],p[:j-1])
            return res
        # examples like 
        else:
            if s == "":
                return isMatch(s, p[:j-1])
            k = i if i>=0 else 0
            # Skip the duplicate characters
            while s[k] == flag and k >= 0:
                k -= 1
            #print k, i
            res = False
            print i,k
            for n in range(k+1,i+2):
                #print n, "s:", s[:n], "p:", p[:j-1]
                res = res or isMatch(s[:n], p[:j-1])
            return res
                
print isMatch("aab", "b.*")