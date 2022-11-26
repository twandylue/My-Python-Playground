import os
import subprocess
import shutil
from pprint import pprint

command = "echo 'hello'"
result = subprocess.run(command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(result.stdout)
print(result.stderr)
