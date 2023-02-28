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

# Define a list of source and destination directories
directories = [
	{
		'srcdir': '/home/ajinkya/Desktop/',
		'dstdir': '/media/ajinkya/BackupDisk/Desktop_Backup/'
	},
	{
		'srcdir': '/media/ajinkya/Ajinkya-Data/',
		'dstdir': '/media/ajinkya/BackupDisk/DataSSD_Backup/'
	}
]

# Loop through the list of directories and sync each pair
for directory in directories:
	srcdir = directory['srcdir']
	dstdir = directory['dstdir']
	
	# Check if the source and destination directories exist
	check_directory(srcdir)
	check_directory(dstdir)
	
	# Delete the contents of the destination directory
	empty_directory(dstdir)
	
	# Sync the directories
	sync_directories(srcdir, dstdir)
	
	print()

########################################################################################

# Print a message indicating that the script has finished executing
print()
print("All Done!")
print()

########################################################################################
