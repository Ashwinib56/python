# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:53:09 2022

@author: cse
"""


import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('C:/olympic/athlete_events.csv')
plt.hist(data['Age'])
plt.xlabel('Age')
plt.show()