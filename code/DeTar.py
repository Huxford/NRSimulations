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
import tarfile
import os

# defining constants
PI =  np.pi
allfreq=[]
freq_arr=np.transpose(allfreq)
#===============================================================================
#  Go through and rename files
#===============================================================================
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

count=1
for file in os.listdir('.'):
  if file.endswith(".tar"):
    tar = tarfile.open(file)
    tar.extractall()
    tar.close()
    os.rename(find("metadata.txt", '.'),"NRFile_%s.txt"%(count))
    os.rename(find("data.h5",'.'),"Data_%s.h5"%(count))
    count=count+1





