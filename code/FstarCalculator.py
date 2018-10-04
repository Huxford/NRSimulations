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
import h5py
from scipy import signal
import os
import glob
# defining constants
PI =  np.pi

#===============================================================================
# Calculate f*
#===============================================================================
def Max_Freq(filename,Mass1,Mass2,Lambda,l1,l2,filenumber):
  count=0
  freq_file=[];max_amp=[]
  lambda_file=[];l1_file=[];l2_file=[]
  f = h5py.File(filename, 'r')
  Mass=Mass1+Mass2
  list=f.keys()
  
# Get all data from NR .h5 files (22 mode)
  if 'rh_22' in list:
    group=f['rh_22']
    list=group.keys()
    for n in list:
      if n[0:8]=='Rh_l2_m2':
          data=group.get(n)
      else:
        continue



#Calculations for f*
#u/M:0 Reh/M:1 Imh/M:2 Redh:3 Imdh:4 Momega:5 A/M:6 phi:7 t:8

      u=data[0::,0];hp=data[0::,1];hc=data[0::,2];freq=data[0::,5];phi=data[0::,7]

      env=(hc**2 + hp**2)**.5
      t=(u*Mass*MTSUN_SI)

      max_amp_tuple=np.where(env==max(env))
      max_amp_index=max_amp_tuple[0]

      max_amp_time=t[max_amp_index]
      dt=t[1]-t[0]
      phase = np.unwrap(np.angle(hp+1j*hc))
      dphi = -np.gradient(phase)/dt
      frequency = dphi/(2.*np.pi)
      max_amp_freq=frequency[max_amp_index]
      freq_file.append(max_amp_freq)
      lambda_file.append(Lambda)
      l1_file.append(l1)
      l2_file.append(l2)
#Plot the waveform if needed

#plt.figure()
#plt.plot(t,hc)
    #plt.scatter(max_amp_time,freq[max_amp],s=100)
    #plt.scatter(max_amp_time,env[max_amp_index],s=3)
    #plt.scatter(t[max_amp],env[max_amp],s=3,c='b')
    #plt.plot(t,env,c='r')
    #plt.savefig('Test%s%s'%(fileprefix,n[:-3]))

      np.savetxt("Freq22NoSpin_arr%s.txt" %(filenumber),freq_file)
      np.savetxt("Lambda22NoSpin_arr%s.txt" %(filenumber),lambda_file)
      np.savetxt("Lambda1NoSpin_arr%s.txt" %(filenumber),l1_file)
      np.savetxt("Lambda2NoSpin_arr%s.txt" %(filenumber),l2_file)

  else:
    print(filename)
#===============================================================================
# Cycle through Data Files & Feed Metadata to Function
#===============================================================================
filenumbers=[]
for name in glob.glob("*.txt"):
        if name[0:6]=="NRFile":
            
              fileprefix=name.rpartition('.')[0]
              filenumber=fileprefix.rpartition('_')[2]
              filenum=float(filenumber)
              filenumbers.append(filenum)
              metadata=open('%s.txt'%(fileprefix),'r')
              for line in metadata.readlines():
                  label=line.split(' ')[0]
                  if label == 'id_mass_starA':
                      m1=float(line.split('=')[1])
                  if label == 'id_mass_starB':
                      m2=float(line.split('=')[1])
                  if label == 'id_Lambda':
                      Lambda=float(line.split('=')[1])
                  if label == 'id_spin_starA':
                      spinA=float(line.split(',')[2])
                  if label == 'id_spin_starB':
                      spinB=float(line.split(',')[2])
                  if label == 'id_Lambdaell_starA':
                      newline=(line.split(',')[0])
                      l1=float(newline.split('=')[1])
                  if label == 'id_Lambdaell_starB':
                      newline=(line.split(',')[0])
                      l2=float(newline.split('=')[1])
              if spinA == 0. and spinB == 0.:
                print(filenumber)
              else:
                continue
              


              Max_Freq('Data_%s.h5'%(filenumber),m1,m2,Lambda,l1,l2,filenumber)

