import os
import sys

mode = "GUI"
id = sys.argv[1]
gen = sys.argv[2]
os.system("python3 simulate.py " + mode + " " + id + " "+ gen)
