# CS396ArtificialLife Winter 2023
# Joshua K Lee (JKL4323)


#### INFO ####
In this assignment, we are asked to randomly generate a 1d morphology

### STEPS ###
In order to randomly generate a 1d morphology such as a snake, I wanted to first randomly generate the position of the first link of the creature.

The first link is very important as the first link and position are absolute in pybullet, this means that for any subsequent links/joints, it would be relative to the link/joint upstream to it.

Below is a diagram that shows this.

![Alt text](/jointdiagram.pngraw=true "Title")

After randomly generating the first link and joints positions, I am able to run a loop for a randomly generated number of links where I randomly generate a link and a joint, and am able to connect them to previous joints by saving that information.

The links are different colored as ones that are green have sensors on them and ones that are cyan do not.
These are randomly generated and allow the snake to have random movement and behavior.


#### TO RUN ####
1. Switch to branch a6try4
2. Run python3 search.py
