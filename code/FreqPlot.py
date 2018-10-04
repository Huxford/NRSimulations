#===============================================================================
#  Imports
#===============================================================================
#! /usr/bin/env python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import random
import h5py
import os
from numpy.polynomial.polynomial import polyfit
#===============================================================================
#  Read in Mass and Lambda Files
#===============================================================================

Lambda1=[];Lambda2=[];Mass1=[];Mass2=[];Freq_arr=[];Tilda_arr=[];FLSO_arr=[];FreqSpin_arr=[];TildaSpin_arr=[]


freqData= open('AllFreqSpinArr.txt','r')
for line in freqData.readlines():
    FreqSpin_arr.append(float(line.split(' ')[0]))

lambdaData= open('AllLambdaSpinArr.txt','r')
for line in lambdaData.readlines():
    TildaSpin_arr.append(float(line.split(' ')[0]))

freqSData=open('AllFreqNoSpinArr.txt','r')
for line in freqSData.readlines():
    Freq_arr.append(float(line.split(' ')[0]))

lambdaSData=open('AllLambdaNoSpinArr.txt','r')
for line in lambdaSData.readlines():
    Tilda_arr.append(float(line.split(' ')[0]))


index_arr=[]
index_arrS=[]
for index in range(0,len(Freq_arr)):
  if Freq_arr[index]>= 2400:
    index_arr.append(index)
    print(Freq_arr[index])
    print(index)
for index in range(0,len(FreqSpin_arr)):
  if FreqSpin_arr[index]<0:
    index_arrS.append(index)
    print(FreqSpin_arr[index])
    print(index)


for index in sorted(index_arr, reverse=True):
  del Freq_arr[index]; del Tilda_arr[index]
for index in sorted(index_arrS, reverse=True):
  del FreqSpin_arr[index]; del TildaSpin_arr[index]



print(len(Tilda_arr),len(Freq_arr))
print(len(TildaSpin_arr),len(FreqSpin_arr))
#===============================================================================
#  Create numpy arrays of integers
#===============================================================================
lambda1_arr=np.array(Lambda1)
lambda2_arr=np.array(Lambda2)
mass1_arr=np.array(Mass1)
mass2_arr=np.array(Mass2)
freq_arr=np.array(Freq_arr)
tilda_arr=np.array(Tilda_arr)
fLSO_arr=np.array(FLSO_arr)
tildaspin_arr=np.array(TildaSpin_arr)
freqspin_arr=np.array(FreqSpin_arr)
freq_total=np.append(freqspin_arr,freq_arr)
tilda_total=np.append(tildaspin_arr,tilda_arr)

tilda_15=tilda_arr**.2
tildaspin_15=tildaspin_arr**.2
tildatotal_15=tilda_total**.2

lambda_mesh=np.linspace(2.6,5.1,166)
freq_mesh=np.linspace(1100,2200,266)
tilda_fit=(10**(3.69652-(0.131743*lambda_mesh)))
#===============================================================================
#  Create a best fit line
#===============================================================================
b, m,c= polyfit(freq_total, tildatotal_15, 2)
x,y,z= polyfit(freq_arr, tilda_15, 2)


#===============================================================================
#  Generate Histograms and Plots
#===============================================================================
plt.figure()
plt.scatter(tilda_15,Freq_arr, label='NR without Spin', s=4)
plt.scatter(tildaspin_15,freqspin_arr, label='NR with Spin', s=4, c='cyan')
plt.scatter(2.88,1800,label='170817',s=4,c='g')
plt.plot(lambda_mesh,tilda_fit, c='r',label='Read Fit')
plt.plot(b +m*freq_mesh + c*(freq_mesh**2), freq_mesh, c='y',label="NR Fit") #y=%.2f+%.4fx+%.4fx^2"%(b,m,c))
#plt.plot(x +y*freq_mesh + z*(freq_mesh**2), freq_mesh, c='purple',label="NR Non-Spinning Fit")
print("y=%f+%fx"%(b,m))
plt.xlabel("$\widetilde{\Lambda}^{1/5}$")
plt.ylabel("$f^*$ (Hz)")
plt.legend()
plt.savefig("FreqvTildeNRFit2")
plt.show()

