import sys
import os
import shutil

source = sys.argv[1]
version = sys.argv[2]

lst = os.listdir(source)

def funk(lst, version):
    version = version.split(".")
    version = list(map(int, version))
    lst_new = []
    for i in lst:
        v = i.split('_')[1]
        v = v.split('.')
        v = list(map(int, v))
        if(version > v):
            lst_new.append(i)
    return lst_new

lst_new = funk(lst, version)

for i in lst_new:
    shutil.rmtree(f"{source}/{i}")