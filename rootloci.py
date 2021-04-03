# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:23:56 2021

@author: Administrator
"""

from control import *
from matplotlib import pyplot as plt

'''
    G(s)H(s) = K*1/(4s^3 + 4s^2 + s)
'''

#sy1 = tf([1], [4,4,1,0])
sy1 = tf([1,4],[1,1,-2])
rlocus(sy1)
plt.show()