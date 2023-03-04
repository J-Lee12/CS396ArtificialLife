import os
import sys

mode = "GUI"
temp = sys.argv[1]
gen = sys.argv[2]
os.system("python3 simulate.py " + mode + " " + temp + " "+ gen)
