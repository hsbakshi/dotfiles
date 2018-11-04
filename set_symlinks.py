#!/usr/bin/env python3
""" 
    This script symlinks default linux settings files 
    to files in this directory.
    WARNING: Running this script will replace your original settings
    files (~/.vimrc etc) with symlinks. Backup those files if you need
    them.
    Versions: Python2.5 and above
"""
import os
import subprocess
import sys

EXCLUDES = ["README", "set_symlinks.py"]

def get_file_list():
    """ Returns list of files in current directory.
    """
    lscomm = subprocess.Popen(['ls'], stdout=subprocess.PIPE)
    files = lscomm.stdout.readlines()
    lscomm.stdout.close()
    return files

def set_symlink(fname):
    """ Sets the '.fname' file in home directory as symlink
        to the fname file in current directory.
    """
    home_dir = os.path.expanduser("~")
    default_path = os.path.join(home_dir, "."+fname)
    repo_path = os.path.join(sys.path[0], fname)
    print('Setting symlink for', fname, '...',)
    if os.path.exists(default_path):
        os.remove(default_path)
    try:
        os.symlink(repo_path, default_path)
        print('done.')
    except Exception as e:
        print('\nUnable to create symlink for', fname)
        print(type(e))
        print(e.args,'\n')

if __name__ == "__main__":
    files = get_file_list()
    for fname in files:
        fname = fname.decode("utf-8")
        fname = fname.rstrip()
        if fname not in EXCLUDES:
            set_symlink(fname)
