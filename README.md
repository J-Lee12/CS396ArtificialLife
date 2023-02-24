# CS396ArtificialLife Winter 2023
# Joshua K Lee (JKL4323)


#### INFO ####
In this assignment, we are asked to randomly generate a 1d morphology

### STEPS ###
In order to randomly generate a 3d morphology, I wanted to first randomly generate the position of the first link of the creature.

The first link is very important as the first link and position are absolute in pybullet, this means that for any subsequent links/joints, it would be relative to the link/joint upstream to it.

Below is a diagram that shows this.

![My Image](/jointdiagram.png)

In order to create a 3d creature, at each step the creature must randomly choose which direction to grow in. 
The creature decides which direction to grow in randomly however, the joint placement gets a bit complicated in this case.

In the below figure that I drew up we can see that if a link grows straight it is straight forward.
The joint is located at the prior links length/2

However, in the case that it decides to branch off another way then, it must have the information of which ever side's length it wants to grow to. In this example if the creature wants to grow to the right, then it must place a joint at the prior links xlength/2 and ylength/2

![My Image](/IMG_0889.jpeg)

The links are different colored as ones that are green have sensors on them and ones that are cyan do not.
These are randomly generated and allow the figure to have random movement and behavior.

### The way this works ###

1. we call search.py, it creates an instance of the parallel hillclimber
2. we evaluate the parents
2. Then we evolve the first parents
    3. to evolve, we first spawn children by deep copying the parents and then assigning them new ids
    4. We then randomly modify part of the weights in the brain to change the fitness score
    5. print the fitness
    6. we pick whether or not the parent or the child had a better fitness
7. repeat



#### TO RUN ####
1. Switch to branch a6try4
2. Run python3 search.py


###  Credits ###
CS396 Artificial Life - Prof Sam Kriegman
LudoBots Tutorial - https://www.reddit.com/r/ludobots/
