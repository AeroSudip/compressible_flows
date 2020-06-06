# -*- coding: utf-8 -*-
"""
This is a block code for computing OSW properties
"""

# The code takes inflow Mach number and gas properties

print('This Is The Fight Of Our Lives. We Are Going To Win. Whatever It Takes.')


import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
from sympy import*

# Flow
M_1 = 6;
gamma = 1.37
gamman = (gamma-1)
gammap = (gamma+1)
rad = np.pi/180
deg = 1/rad

# wedge
theta = 12.5*rad
beta_min = np.arcsin(1/M_1)

betai = np.arange(beta_min,np.pi/2,np.pi/200000)

i=0
betas  = np.zeros((betai.shape))
error = np.zeros((betai.shape))
for k in range(1,betai.size):
    beta = betai[k]
    error[k] = np.tan(beta)/np.tan(beta-theta) - gammap*(M_1*np.sin(beta))**2 / (2+gamman*(M_1*np.sin(beta))**2)
    error = abs(error)
    if error[k] < 0.0002:
        break
    #returns the shock angle beta
print('beta = ',beta*deg, 'degrees')

# post-OSW properties
sigma = np.tan(beta)/np.tan(beta-theta); # density ratio (increment) across OSW
print('Density ratio = ',sigma)
