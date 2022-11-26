import os
import subprocess
import shutil
from pprint import pprint

my_cwd = os.getcwd();
print(my_cwd)

dir_list = os.listdir();
for i in dir_list:
    print(i)

print(dir_list)

print(os.path.split(os.getcwd()))

shutil.copyfile('test.py', 'test2.py')
