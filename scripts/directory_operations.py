import os
import subprocess
import shutil
from pprint import pprint

my_cwd = os.getcwd();
print(my_cwd)

dir_list = os.listdir();
# for i in dir_list:
#     print(i)

print(dir_list)

print('------ ### ------')

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

with cd("../"):
    # subprocess.call("pwd")
    dir_list = os.listdir();
    print(dir_list)
    print(os.getcwd())
    subprocess.call("tree")
