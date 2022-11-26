import os
import subprocess
import shutil
from pprint import pprint

my_cwd = os.getcwd();
print(my_cwd)

shutil.copyfile('file_operations.py', 'test2.py')
