#===============================================================================
#  Imports & Set-Up
#===============================================================================

import lalsimulation as lalsim
import lal
from lal import MTSUN_SI, PC_SI, C_SI
from operator import add
import numpy as np
import subprocess
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import h5py
import tarfile
import os
import glob



# defining constants
PI =  np.pi
allfreq=[]
freq_arr=np.transpose(allfreq)
#===============================================================================
#  Go through and rename files
#===============================================================================
M1=np.array([]);M2=np.array([]);Lambda=np.array([]);Spin1=np.array([]);Spin2=np.array([]);L1=np.array([]);
L2=np.array([]);

for name in glob.glob("*.txt"):
    #if name[-3:]==".h5" or name[-4:]==".txt":
    if name[-4:]==".txt":
            fileprefix=name.rpartition('.')[0]
            metadata=open('%s.txt'%(fileprefix),'r')
            for line in metadata.readlines():
                label=line.split(' ')[0]
                if label == 'id_mass_starA':
                    m1=float(line.split('=')[1])
                    M1=np.append(M1,m1)
                if label == 'id_mass_starB':
                    m2=float(line.split('=')[1])
                    M2=np.append(M2,m2)
                if label == 'id_Lambda':
                    Lambda_Tilda=float(line.split('=')[1])
                    Lambda=np.append(Lambda,Lambda_Tilda)
                if label == 'id_spin_starA':
                    spinA=float(line.split(',')[2])
                    Spin1=np.append(Spin1,spinA)
                if label == 'id_spin_starB':
                    spinB=float(line.split(',')[2])
                    Spin2=np.append(Spin2,spinB)
                if label == 'id_Lambdaell_starA':
                    newline=(line.split(',')[0])
                    l1=float(newline.split('=')[1])
                    L1=np.append(L1,l1)
                if label == 'id_Lambdaell_starB':
                    newline=(line.split(',')[0])
                    l2=float(newline.split('=')[1])
                    L2=np.append(L2,l2)

Master_array=[M1,M2,L1,L2,Spin1,Spin2,Lambda]

plt.figure()
fig, ax = plt.subplots(nrows=7, ncols=7, sharex='col', sharey='row', figsize=(10, 10))

for row in range(0,7):
    for column in range(0,7):
        if row > column:
          continue
        else:
          ax[column,row].scatter(Master_array[row],Master_array[column],s=1)

ax[0,0].set(ylabel='Mass 1')
ax[1,0].set(ylabel='Mass 2')
ax[2,0].set(ylabel='Lambda 1')
ax[3,0].set(ylabel='Lambda 2')
ax[4,0].set(ylabel='Spin 1')
ax[5,0].set(ylabel="Spin 2")
ax[6,0].set(ylabel="Lambda",xlabel='Mass1')
ax[6,1].set(xlabel='Mass 2')
ax[6,2].set(xlabel='Lambda 1')
ax[6,3].set(xlabel='Lambda 2')
ax[6,4].set(xlabel='Spin 1')
ax[6,5].set(xlabel='Spin 2')
ax[6,6].set(xlabel='Lambda')


plt.legend()
plt.savefig('Test4')



