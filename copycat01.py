#!/usr/bin/env python3
import shutil
import os

# move into the working director
os.chdir("/home/student/mycode/")

# copy the first file to the second
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
# copy the entire first directory to the second
shutil.copytree("5g_research/", "5g_research_backup/")

