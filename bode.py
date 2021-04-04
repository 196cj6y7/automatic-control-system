# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 21:17:56 2021

@author: Administrator
"""
from scipy import signal
import matplotlib.pyplot as plt
from sympy import *
import sympy as sym


s = symbols('s')
'''

G(s) = 50*(s+2)/(s**2 + 4*s + 100) / s


'''

sys = signal.TransferFunction([50,100],[1,4,100,0])
w, mag, phase = signal.bode(sys)


plt.figure()
plt.subplot(211)
plt.title('Bode plot')

plt.ylabel('dB')
plt.semilogx(w, mag, color='orange')


plt.subplot(212)
plt.ylabel('deg')
plt.semilogx(w, phase)
plt.show()
