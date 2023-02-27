#!/usr/bin/env python3

# Run this script as: python /home/ajinkya/Desktop/RsyncProgram/MainProgram.py

import os
import shutil
from tqdm import tqdm
import datetime

import sys
# Don't generate the __pycache__ folder locally
sys.dont_write_bytecode = True 
# Print exception without the buit-in python warning
sys.tracebacklimit = 0 

########################################################################################

from modules import *

########################################################################################

# Define the source and destination directories
srcdir1 = "/home/ajinkya/Desktop/"
dstdir1 = "/media/ajinkya/Ajinkya/Desktop_Backup/"

srcdir2 = "/media/ajinkya/Ajinkya-Data/"
dstdir2 = "/media/ajinkya/Ajinkya/DataSSD_Backup/"

########################################################################################

# Check if the source and destination directories exist
for srcdir, dstdir in [(srcdir1, dstdir1), (srcdir2, dstdir2)]:
	if not os.path.isdir(srcdir):
		print(f"Error: {srcdir} does not exist")
	elif not os.path.isdir(dstdir):
		print(f"Error: {dstdir} does not exist")
	else:
		sync_directories(srcdir, dstdir)

# Delete the contents of dstdir1 and dstdir2
for dstdir in [dstdir1, dstdir2]:
	if os.path.isdir(dstdir):
		shutil.rmtree(dstdir)
		os.makedirs(dstdir)

########################################################################################

# Print a message indicating that the script has finished executing
print("")
print("All Done!")
print("")

########################################################################################
