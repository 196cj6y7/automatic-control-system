# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:03:41 2021

@author: Administrator
"""
import numpy as np
from sympy import *
import sympy as sym

s = symbols('s')
G = (s+4)/(s-1)/(s+2)
dG = diff(G, s)

dG = sym.simplify(dG)
g2 = s**2 + s - (s+4)*(2*s+1)-2
print(expand(g2))
print('--------')
print(dG)