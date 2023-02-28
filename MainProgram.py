#!/usr/bin/env python3

# Run this script as: python /home/ajinkya/Desktop/RsyncProgram/MainProgram.py

import os

import sys
# Don't generate the __pycache__ folder locally
sys.dont_write_bytecode = True 
# Print exception without the buit-in python warning
sys.tracebacklimit = 0 

########################################################################################

os.system('clear')

########################################################################################

from modules import *

########################################################################################

# Define the source and destination directories
srcdir1 = "/home/ajinkya/Desktop/"
dstdir1 = "/media/ajinkya/BackupDisk/Desktop_Backup/"

srcdir2 = "/media/ajinkya/Ajinkya-Data/"
dstdir2 = "/media/ajinkya/BackupDisk/DataSSD_Backup/"

########################################################################################

# Check if the source and destination directories exist
check_directory(srcdir1)
check_directory(dstdir1)
check_directory(srcdir2)
check_directory(dstdir2)

# Delete the contents of dstdir1 and dstdir2
empty_directory(dstdir1)
empty_directory(dstdir2)

print()

# Sync the directories
sync_directories(srcdir1, dstdir1)
sync_directories(srcdir2, dstdir2)

########################################################################################

# Print a message indicating that the script has finished executing
print()
print("All Done!")
print()

########################################################################################
