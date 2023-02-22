
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

    """
    errors = []  # List to store any error messages

    try:
        # Create a new directory in the destination with a timestamp
        timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        new_dstdir = os.path.join(dstdir, f"Backup_{timestamp}")
        os.makedirs(new_dstdir, exist_ok=True)

        # Check if there is enough space in the destination directory
        available_space = shutil.disk_usage(new_dstdir).free
        source_size = shutil.disk_usage(srcdir).used

        if available_space < source_size:
            raise Exception(f"Not enough space in {new_dstdir} to copy {srcdir}")

        # Sync the directory and display a feedback message
        print(f"\nSyncing {srcdir} directory...\n")

        # Use tqdm to display a progress bar
        files_copied = 0
        total_files = 0

        for root, dirs, files in os.walk(srcdir):
            total_files += len(files)

        with tqdm(total=total_files) as pbar:
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

                    files_copied += 1
                    pbar.update(1)

        print(f"\n{srcdir} directory synced to {new_dstdir}\n")

    except Exception as e:
        error_msg = f"Error syncing {srcdir} directory: {e}"
        print(error_msg)
        errors.append(error_msg)

    # Dump any error messages to a file
    if errors:
        error_file_name = f"Errors_{timestamp}.txt"
        with open(error_file_name, "w") as f:
            f.write("\n".join(errors))
        print(f"{len(errors)} error messages written to {error_file_name}")

########################################################################################