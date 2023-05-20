# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:46:25 2023

@author: parth
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import math #needed for definition of pi
x = np.arange(0,math.pi*2,0.05)
y = np.sin(x)
plt.plot(x,y)
plt.xlabel("angle")#x label
plt.ylabel("sine")# y label
plt.title("sine wave")
plt.show()

from numpy import *
x = linspace(-3,3,15) # linespace(staring , ending , total points )
y= x**2
plt.plot(x,y)
plt.scatter(x,y)
plt.show()