import os
import shutil

working_dir = os.path.dirname(os.path.realpath(__file__)) # path to the folder containing this file
os.chdir(working_dir)

shutil.copyfile("VER_0/sfc/ys_chip0.hex","Tools/ys_chip0.hex")

os.system("python3 Tools/createSource/createSource.py")