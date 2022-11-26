import os
import subprocess
import shutil
from pprint import pprint

command = "echo 'hello'"
# WARNING: before Python 3.7:
# result = subprocess.run(command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result = subprocess.run(command.split(' '), capture_output=True)
print(result.stdout)
print(result.stderr)
print(result.returncode)

# multiple commands
command2 = "echo a1; echo b2; ls"

result2 = subprocess.run(command2, capture_output=True, shell=True)
print(result2.stdout.decode())
print(result.returncode)
