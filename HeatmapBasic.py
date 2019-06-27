# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=abs(np.random.normal(loc=50,size=(50,50), scale=100))
#datay=abs(np.random.normal(loc=25,size=50, scale=50))

print(data)
ax=plt.subplot()
title="Heatmap"
ax.set_xticks([])
ax.set_yticks([])
sb.heatmap(data,cmap='RdYlGn',linewidths=0.30,ax=ax)
plt.show()