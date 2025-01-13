from os.path import isdir
import tarfile
from pathlib import Path as path
import os
from this import d

print(d)

home = path.home()

def encryptfolder(yourfolder):
    with tarfile.open(f"{home}/vault/vault.tar", "x") as tar:
        tar.add(yourfolder)
    print(yourfolder)

def somefunc():
    for file in os.listdir("./"):
        if file.endswith("tar"):
            print(2)

def makedir():
    os.mkdir(f"{home}/vault")

if isdir(f"{home}/vault"):
    print(1)
else:
    makedir()

