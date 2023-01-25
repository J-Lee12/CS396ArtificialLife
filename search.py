import os

from hillclimber import HILLCLIMBER

hc = HILLCLIMBER()
hc.Evolve()
hc.Show_Best()

# i = 0
# while i < 5:
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")
#     i += 1

