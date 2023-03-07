# CS396ArtificialLife Winter 2023
# Joshua K Lee (JKL4323)


## Info
For the final Project for CS396 - Artificial Life at Northwestern University, we are asked to not only randomly generate a 3d morphology, but to also evolve it for locomotion through evolving both the brains and the body. In this case the locomotion that we are aiming for is one that moves to the left "away" from the viewer.

## Randomly Generating The Body
###### Joints
In order to randomly generate a 3d morphology, I wanted to first randomly generate the position of the first link of the creature.

The first link is very important as the first link and position are absolute in pybullet, this means that for any subsequent links/joints, it would be relative to the link/joint upstream to it.

In order to create a 3d creature, at each step the creature must randomly choose which direction to grow in. 
The creature decides which direction to grow in randomly however, the joint placement gets a bit complicated in this case.

However, in the case that it decides to branch off another way then, it must have the information of which ever side's length it wants to grow to. In this example if the creature wants to grow to the right, then it must place a joint at the prior links xlength/2 and ylength/2. This is demonstrated the figure below.

<img src="/images/IMG_0889.jpeg" width="500" height="500">


The links are different colored as ones that are green have sensors on them and ones that are cyan do not.

###### Links

In order to randomly generate the links I used a random float generator from numpy.
Using this allowed me to create links of random sizes in the x,y,z directions. 

Below are examples of what are possible. 

<img src="/images/possible1.png" width="400" height="400"> <img src="/images/possible2.png" width="400" height="400">
<img src="/images/possible3.png" width="400" height="400"> <img src="/images/possible4.png" width="400" height="400">

However in order to prevent a 3d snake like creature, everytime I added a link in a different direction then what the previous link was in, I added a link to a random face to the opposite side. This resulted in the 3d creatures shown above.

As can be shown in the diagrams, some links are green and some are cyan. The ones that are green are links that contains sensor neurons. The cyan ones are normal links. 

## Randomly Generating the Brain

The brain has a neural network that allows the creature to not only act, and sense, but to allow its sensors to be able to influence the way that it acts. 

In this 3d Morphology, at each point when a link is created there it is randomly decided whether or not if a link will be a sensor or not, however every joint becomes a motor neuron. 

The brain has an a two dimensional array that contains the weights for each synapse. 
This array's values are created by random but then scaled to be within [-1,+1]

**add a diagram of the brain here**

## Fitness

The fitness is evaluated by obtaining the last position of the robot.
We do this by obtaining the last x position of the robot.

Because we are looking for the robot to be moving "away" in the x direction that means that we are looking for a negative fitness as we want a negative displacement.

**insert a screenshot of the simulator**

## Mutating the Brain

To mutate the brain, what happens is that we deepcopy the parent to have an exact copy of the parent that has no references to the original parent. This allows us to randomly modify the child such that it doesn't modify the parent.

In each generation we randomly modify a synapse in the child's weights. This causes the fitness to differ between the parent and the child. 

**Selection occurs by comparing the parent and child's fitness and selecting whichever one had a more negative value**

An example being

![My Image](/images/fitness.png)

In this case we would choose the parent in both generations because they had lower fitnesses than their children.
When we choose the parent that means that the copy would come from the parent rather than the child.

## Mutating the Body

Much like how we did in the brain, once we deepcopy the parent, we have access to the data that creates the body.
**Selection occured by replacing the first link of the body (the one farthest away from the viewer) with another randomly sized link to see if it would help the robot in evolution**

Below is an example of a non evolved vs evolved As can be shown the first block is taller and slightly wider than the block in the first image.

<img src="/images/notevolved.png" width="400" height="400"> <img src="/images/evolved.png" width="400" height="400">

## Data

I stored the data of 5 different runs of having 25 Generations and 100 Rounds of Generation.
However as mentioned, because the goal was to evolve to get more and more negative fitness scores the graph would been inverse, so I multiplied all values by -1 so that values would appear as though they grew.

![My Image](/images/plot.png)

As can be shown, each seed was able to evolve and arrive at a solution that would create a robot that moved it to the left "away" from the viewer

## The way the simulator works
1. we call search.py, it creates an instance of the parallel hillclimber
2. we evaluate the parents (do this step population size times)
    3. We run Run_Simulation()
    4. This calls the robot constructor with the specified ID
        5. Robot gets the sensor values and updates its neural network values to what is included in brainID.nndf
        6. The robot then acts based on the values given
        7. prints the fitness of that robot in a file
    8. We then create a copy of the parent and then mutate it
    9. after doing steps a-e again, we check if the children or parent had a better fitness and select the one that did

10. Run steps 3-9 Generationsize times
11. Select the robot that had the best fitness and then simulate that one.




#### TO RUN ####
1. Switch to branch finalproject-try1
2. To change the number of generations and the population size, change the variables NumberofGenerations and populationSize in constants.py
3. Run 
```bash
python3 search.py
```
4. To visualize the graph, edit plot.py to read in the numpy files that you decided to name them and the legends accordingly
5. Run
```bash
python3 plot.py
```
### To Resimulate ###
1. open bestid.txt to find which id had the best fitness
2. To simulate the first body of that id, Run
```bash
python3 replay.py id 0
```
3. To simulate the final body of that id you must know the number of the last gen
```bash
python3 replay.py id gen
```



###  Credits ###
CS396 Artificial Life - Prof Sam Kriegman
LudoBots Tutorial - https://www.reddit.com/r/ludobots/
