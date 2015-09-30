# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:06:35 2015

@author: yys
"""

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    res = ""
    dict = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
    # 1000 ~ 9999
    a,num = divmod(num, 1000)
    res += a*'M'
    # 100 ~ 999
    b,num = divmod(num,100)
    if b == 4:
        res += 'CD'
    elif b == 9:
        res += 'CM'
    elif b < 4:
        res += b*'C'
    else :
        res += 'D'+(b-5)*'C'
    # 10 ~ 99
    c,num = divmod(num,10)
    if c == 4:
        res += 'XL'
    elif c == 9:
        res += 'XC'
    elif c < 4:
        res += c*'X'
    else :
        res += 'L'+(c-5)*'X'
    # 1 ~ 9
    if num != 0:
        res += dict[num]
    return res
    
print intToRoman(1435)