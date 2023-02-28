## Directory Synchronization Script

This is a Python script that synchronizes the contents of two directories by copying the files and directories from a source directory to a destination directory. The script can be used to backup important files and data to an external drive or to synchronize data between two computers.

### Features

The script has the following features:

- Copies the contents of a source directory to a new subdirectory within a destination directory.
- Checks if there is enough space in the destination directory to copy the source directory.
- Uses the `tqdm` package to display a progress bar during the copying process.
- Creates an error file if any errors occur during the copying process.
- Empties the contents of the destination directory before copying the source directory.
- Checks if the source and destination directories exist before copying the source directory.

### Requirements

The script requires the following Python packages to be installed:

- `os`
- `shutil`
- `tqdm`
- `datetime`

### Usage

To use the script, follow these steps:

1. Open the `MainProgram.py` file in a text editor or IDE.
2. Modify the `srcdir1`, `dstdir1`, `srcdir2`, and `dstdir2` variables to specify the source and destination directories that you want to synchronize.
3. Save the file and run the script using the command `python MainProgram.py` in a terminal or command prompt.

### Notes

- The script clears the terminal screen at the beginning of execution using the `os.system('clear')` command. If you are using Windows, replace `'clear'` with `'cls'`.
- The script deletes the contents of the destination directories before copying the source directories. Make sure that you have a backup of any important files in the destination directories before running the script.
- The script creates a new subdirectory within the destination directory with a timestamp to store the backup of the source directory. The subdirectory is named `Backup_<timestamp>`.
- The script creates an error file named `Errors_<timestamp>.txt` in case any errors occur during the copying process. The file is saved in the same directory as the script.
- The script checks if the source and destination directories exist before copying the source directory. If a directory does not exist, the script raises a `NotADirectoryError` exception.
- The script was tested on Linux and should work on Windows and macOS as well.

### License

This script is licensed under the [GPL-3.0 license](https://www.gnu.org/licenses/gpl-3.0.en.html).
