#!/usr/bin/env python3

import shutil
import os

# force the Python program to start in the home user directory from any location on the system
os.chdir('/home/student/mycode/')

# move the file at the path source to the path destication and return a absolute
# path string of the new location. If it points to a folder, the source gets moved
# into the destination but keeps its current file name
shutil.move('raynor.obj', 'ceph_storage/') # if raynor.obj existed, it would be overwritten
xname = input('What is the new name for kerrigan.obj? ')

# rename the current kerrigan.obj file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


