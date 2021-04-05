# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:23:56 2021

@author: Administrator
"""

from control import *
from matplotlib import pyplot as plt
def plotRootloci(transferFunction):      
    rlocus(transferFunction)
    plt.title('rootloci')
    plt.xlabel('Re(s)')
    plt.ylabel('Im(s)')
    plt.show()
    
'''
    G(s)H(s) = K*1/(4s^3 + 4s^2 + s)
'''

G = tf([1,4],[1,1,-2])
plotRootloci(G)

