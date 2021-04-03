# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 21:17:56 2021

@author: Administrator
"""
from scipy import signal
import matplotlib.pyplot as plt

'''
    G(s) = 1 / (s+1)
'''
sys = signal.TransferFunction([1],[1,1])
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