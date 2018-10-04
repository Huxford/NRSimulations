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
import os
import glob

#===============================================================================
# Combine all Freq Arrays into one
#===============================================================================
freqfilenames = []; lambdafilenames=[]; lambda1filenames=[]; lambda2filenames=[]
freqsfilenames = []; lambdasfilenames=[]; lambda1sfilenames=[]; lambda2sfilenames=[]
for file in glob.glob("*.txt"):
    if file[0:14]=='Freq22Spin_arr': #or file[0:13]=='FreqOther_arr':
          freqfilenames.append(file)
          lambdafilenames.append('Lambda22Spin_arr%s'%(file[14::]))
          lambda1filenames.append('Lambda1Spin_arr%s'%(file[14::]))
          lambda2filenames.append('Lambda2Spin_arr%s'%(file[14::]))
    if file[0:16]=='Freq22NoSpin_arr': #or file[0:13]=='FreqOther_arr':
          freqsfilenames.append(file)
          lambdasfilenames.append('Lambda22NoSpin_arr%s'%(file[16::]))
          lambda1sfilenames.append('Lambda1NoSpin_arr%s'%(file[16::]))
          lambda2sfilenames.append('Lambda2NoSpin_arr%s'%(file[16::]))
    else:
          continue

with open('AllFreqNoSpinArr.txt', 'w') as outfile:
    for fname in freqfilenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

with open('AllLambdaNoSpinArr.txt', 'w') as outfile:
    for fname in lambdafilenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
with open('AllLambda1NoSpinArr.txt', 'w') as outfile:
    for fname in lambda1filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
with open('AllLambda2NoSpinArr.txt', 'w') as outfile:
    for fname in lambda2filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

with open('AllFreqSpinArr.txt', 'w') as outfile:
    for fname in freqsfilenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

with open('AllLambdaSpinArr.txt', 'w') as outfile:
    for fname in lambdasfilenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
with open('AllLambda1SpinArr.txt', 'w') as outfile:
    for fname in lambda1sfilenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
with open('AllLambda2SpinArr.txt', 'w') as outfile:
    for fname in lambda2sfilenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
