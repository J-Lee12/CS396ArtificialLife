# CS396ArtificialLife Winter 2023
# Joshua K Lee (JKL4323)


#### INFO ####
I used a fitness function that by accessing the xcoordinate of the linkzero I am able to move my seal to the left (away from the the observer). I accomplished this by mutating generations and saving each simulation into a dictionary that would hold the fitness score of each simulation. In the end, I am looking for the most negative value so that my stingray/seal will move in the -x direction.

#### TO RUN ####
1. Switch to branch assignment5
2. Run python3 search.py
3. To change the number of generations, population size, and the number of sensor/motor neurons edit constants.py
