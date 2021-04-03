# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 17:27:34 2021

@author: Administrator
"""

from sympy import *
import sympy as sym

sym.init_printing()
s = sym.symbols('s')

'''
    X'(t) = AX(t) + Bu(t)
    y(t) = CX(t) + Du(t)
 => G(s) = C * inv(sI-A) * B + D
    G(s) is transfer function of the dynamic equation
    
    
Ex.
            
            | -5   1   0 |          | 0 |
    dx/dt = |  0  -2   1 |  X(t) +  | 0 |U(t)
            | 20  -10  1 |          | 2 |
            
    Y(t) = [1 -1 0] X(t) + [2] U(t) 
'''

A = Matrix([[-5,1,0],[0,-2,1], [20,-10,1]])
B = Matrix([[0],[0],[2]])
C = Matrix([[1,-1,0]])
D = Matrix([2])


I = eye(len(A.shape)+1)
Q = s*I-A
Q = Q**(-1)

G = C*Q*B + D
G = sym.simplify(G)
print(G)

