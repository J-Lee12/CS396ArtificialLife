import os
import sys

mode = "DIRECT"
temp = sys.argv[1]
gen = sys.argv[2]
print(temp)
os.system("python3 simulate.py " + mode + " " + temp + str(gen))
