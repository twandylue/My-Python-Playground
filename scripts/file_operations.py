import os
import subprocess
import shutil
from pprint import pprint

my_cwd = os.getcwd();
print(my_cwd)

shutil.copyfile('file_operations.py', 'test2.py')

f = open("hello.txt","w+")
f.write("hello!")
f.close()

f = open("hello.txt","a+")
f.write("hello again")
f.close()
