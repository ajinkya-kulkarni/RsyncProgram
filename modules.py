
import os
import shutil
from tqdm import tqdm
import datetime

########################################################################################

def sync_directories(srcdir, dstdir):
	"""
	Syncs the contents of a source directory to a destination directory. A new subdirectory is created within the
	destination directory to store the backup of the source directory.

	Parameters:
	srcdir (str): Path to the source directory.
	dstdir (str): Path to the destination directory.

	Returns:
	None

	Raises:
	Exception: If there is not enough space in the destination directory to copy the source directory.
	If any errors occur during copying, an error message will be printed to the console and added to the `errors` list. 
	At the end of the function, any errors in the `errors` list will be dumped to a text file named `Errors_<timestamp>.txt`. 
	If no errors occur, this file will not be created.
	"""

	errors = []  # List to store any error messages

	try:
		# Create a new directory in the destination with a timestamp
		timestamp = datetime.datetime.now().strftime("%d_%b_%Y_%H%M_hrs")
		new_dstdir = os.path.join(dstdir, f"Backup_{timestamp}")
		os.makedirs(new_dstdir, exist_ok=True)

		# Check if there is enough space in the destination directory
		available_space = shutil.disk_usage(new_dstdir).free
		source_size = shutil.disk_usage(srcdir).used

		if available_space < source_size:
			raise Exception(f"Not enough space in {new_dstdir} to copy {srcdir}")

		# Sync the directory and display a feedback message
		print(f"\nSyncing {srcdir} directory to {new_dstdir}\n")

		# Use tqdm to display a progress bar
		total_files = sum(len(files) for _, _, files in os.walk(srcdir))

		with tqdm(total=total_files, desc = 'Syncing files') as pbar:
			for root, dirs, files in os.walk(srcdir):
				for file in files:
					src_file = os.path.join(root, file)
					rel_path = os.path.relpath(src_file, srcdir)
					dst_file = os.path.join(new_dstdir, rel_path)

					os.makedirs(os.path.dirname(dst_file), exist_ok=True)
					try:
						shutil.copy2(src_file, dst_file)
					except Exception as e:
						error_msg = f"Error copying file {src_file}: {e}"
						print(error_msg)
						errors.append(error_msg)

					pbar.update(1)

		print(f"\n{srcdir} directory successfully synced to {new_dstdir}\n")

	except Exception as e:
		error_msg = f"Error syncing {srcdir} directory: {e}"
		print(error_msg)
		errors.append(error_msg)

	# Dump any error messages to a file
	if errors:
		error_file_name = "/home/ajinkya/Desktop/RsyncProgram/Errors_{}.txt".format(timestamp)
		with open(error_file_name, "w") as f:
			f.write("\n".join(errors))
		print("{} error messages written to {}".format(len(errors), error_file_name))

########################################################################################

def empty_directory(dir_path):
	"""Empty the contents of a directory and all its subdirectories.

	This function recursively deletes all files and subdirectories in the specified directory
	and all its subdirectories. It does not delete the specified directory itself.

	Args:
		dir_path (str): The path of the directory to empty.

	Raises:
		NotADirectoryError: If the specified path does not point to a directory.
	"""
	if not os.path.isdir(dir_path):
		raise NotADirectoryError(f"{dir_path} is not a directory")

	for filename in os.listdir(dir_path):
		file_path = os.path.join(dir_path, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print(f"Error deleting {file_path}: {e}")

	print(f"Successfully emptied {dir_path}")

########################################################################################

def check_directory(directory):
	"""
	Check if a directory exists.

	Args:
		directory (str): The path of the directory to check.

	Raises:
		NotADirectoryError: If the directory does not exist.

	Returns:
		None
	"""
	if not os.path.isdir(directory):
		raise NotADirectoryError(f"{directory} does not exist")

########################################################################################
