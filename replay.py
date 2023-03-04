import os
import sys

mode = "DIRECT"
temp = sys.argv[1]
print(temp)
os.system("python3 simulate.py " + mode + " " + temp)
