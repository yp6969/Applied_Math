# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:59:41 2021

@author: user
"""

import matplotlib.pylab as plt
from matplotlib import cm
import math
import pandas as pd
import numpy as np
import random

plt.style.use('seaborn-whitegrid')
plt.rc('text', usetex=True)
plt.rc('font', family='times')
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.rc('font', size=12)

data = pd.read_csv('car_barcelona.csv', encoding='latin-1')
print(data.columns)

#Create a new column which is the date
data['Date'] = '2013-'+data['Mes de any'].apply(lambda x : str(x))+ '-' + data['Dia de mes'].apply(lambda x : str(x))
data['Date'] = pd.to_datetime(data['Date'])
accidents = data.groupby(['Date']).size()
print('Mean:', accidents.mean(), 'std: ', accidents.std() )
