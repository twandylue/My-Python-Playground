import os
import subprocess
import shutil
from pprint import pprint
import pytest

def add_one(x):
    return x + 1

# Prefix with `test` would be included into pytest execution
def test_answer():
    assert add_one(4) == 5

def test_system_command():
    """Test the exit code of a system command"""
    command = "echo 'hello'"
    result = subprocess.run(command.split(' '), capture_output=True)
    assert result.returncode == 0

# with system exit
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
