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
    print('Setting symlink for %s...' % fname)
    home_dir = os.path.expanduser("~")
    default_path = os.path.join(home_dir, "." + fname)
    repo_path = os.path.join(sys.path[0], fname)
    if os.path.exists(default_path):
        os.remove(default_path)
    try:
        os.symlink(repo_path, default_path)
        print('Done.')
    except Exception as e:
        print('\nUnable to create symlink for %s' % fname)
        print(type(e))
        print(str(e.args) + '\n')

if __name__ == "__main__":
    files = get_file_list()
    for fname in files:
        fname = str(fname.rstrip(), "utf-8")
        if fname not in EXCLUDES:
            set_symlink(fname)
