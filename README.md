                                                    Integrity-Checker
____________________________________________________________________________________________________________________________________________________________________________________________________________________
COMPANY: CODETECH IT SOLUTIONS

NAME: GYANMOTAY VIKAS

INTERN ID: CT12RGV

DOMAIN: CYBER SECURIY

DURATION: 8 WEEKS

MENTOR: NEELA SANTOSH

File Integrity Checker 🔍

Overview

A Python-based file integrity checker that monitors changes in files by computing and comparing hash values. This tool helps ensure file integrity by detecting modifications and newly added files.

Features

✅ Detects file modifications

✅ Identifies new files

✅ Uses SHA-256 for hashing (customizable)

✅ Stores hash values in a JSON file

✅ Simple and lightweight

Installation

Clone the repository and install dependencies:

git clone https://github.com/GYANMOTAYVIKASS
/File-Integrity-Checker.git
cd File-Integrity-Checker
pip install -r requirements.txt

Usage

Run the script and enter the directory path to monitor:

python file_integrity_checker.py

Example Output

New file detected: /path/to/newfile.txt
WARNING: File /path/to/modifiedfile.txt has been modified!
File integrity check completed.

How It Works

The script calculates SHA-256 hashes for all files in the specified directory.

It compares the newly computed hashes with previously stored hashes.

If a file's hash changes, a warning is displayed.

If a new file is detected, it is added to the hash store.

Hash values are saved in file_hashes.json for future comparison.

License

This project is licensed under the MIT License.

Contributions are welcome! Feel free to submit pull requests or open issues to improve the project. 🚀

**OUTPUT

