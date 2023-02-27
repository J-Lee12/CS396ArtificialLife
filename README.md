# CS396ArtificialLife Winter 2023
# Joshua K Lee (JKL4323)


## INFO
In this assignment, we are asked to not only randomly generate a 3d morphology, but to also evolve it for locomotion through evolving both the brains and the body. In this case the locomotion that we are aiming for is one that moves to the left "away" from the viewer.

## Joints
In order to randomly generate a 3d morphology, I wanted to first randomly generate the position of the first link of the creature.

The first link is very important as the first link and position are absolute in pybullet, this means that for any subsequent links/joints, it would be relative to the link/joint upstream to it.

In order to create a 3d creature, at each step the creature must randomly choose which direction to grow in. 
The creature decides which direction to grow in randomly however, the joint placement gets a bit complicated in this case.

However, in the case that it decides to branch off another way then, it must have the information of which ever side's length it wants to grow to. In this example if the creature wants to grow to the right, then it must place a joint at the prior links xlength/2 and ylength/2. This is demonstrated the figure below.

![My Image](/images/IMG_0889.jpeg)

The links are different colored as ones that are green have sensors on them and ones that are cyan do not.

## Links

In order to randomly generate the links I used a random float generator from numpy.
Using this allowed me to create links of random sizes in the x,y,z directions. 

Below are examples of what are possible. 
![My Image](/images/possible1.png) ![My Image](/images/possible2.png) ![My Image](/images/possible3.png) ![My Image](/images/possible4.png)

However in order to prevent a 3d snake like creature, everytime I added a link in a different direction then what the previous link was in, I added a link to a random face to the opposite side. This resulted in the 3d creatures shown above.

As can be shown in the diagrams, some links are green and some are cyan. The ones that are green are links that contains sensor neurons. The cyan ones are normal links. 

## Brain

The brain has a neural network that allows the creature to not only act, and sense, but to allow its sensors to be able to influence the way that it acts. 

In this 3d Morphology, at each point when a link is created there it is randomly decided whether or not if a link will be a sensor or not, however every joint becomes a motor neuron. 

What this means is that we get the following diagram, 

(insert diagram)

The brain has an a two dimensional array that contains the weights for each synapse. 
This array's values are created by random but then scaled to be within [-1,+1]

## Fitness

The fitness is evaluated by obtaining the last position of the robot.
We do this by obtaining the last x position of the robot.

Because we are looking for the robot to be moving "away" in the x direction that means that we are looking for a negative fitness as we want a negative displacement.

## Mutating the Brain

To mutate the brain, what happens is that we deepcopy the parent to have an exact copy of the parent that has no references to the original parent. This allows us to randomly modify the child such that it doesn't modify the parent.

In each generation we randomly modify a synapse in the child's weights. This causes the fitness to differ between the parent and the child. 

We then compare the parent's and child's fitness and select whichever had a more negative fitness.
An example being

![My Image](/images/fitness.png)

In this case we would choose the parent in both generations because they had lower fitnesses than their children.
When we choose the parent that means that the copy would come from the parent rather than the child.

## Mutating the Body

Much like how we did in the brain, once we deepcopy the parent, we have access to the data that creates the body.
To randomly modify body, I replaced the first link of the body (the one farthest away from the viewer) with another random link to see if that would help create a lower fitness. 

Below is an example of a non evolved vs evolved

![My Image](/images/notevolved.png) ![My Image](/images/evolved.png)


## Data

I stored the data of 5 different runs of having 25 Generations and 100 Rounds of Generation.
However as mentioned, because the goal was to evolve to get more and more negative fitness scores the graph would been inverse, so I multiplied all values by -1 so that values would appear as though they grew.

![My Image](/images/plot.png)

As can be shown, each seed was able to evolve and arrive at a solution that would create a robot that moved it to the left "away" from the viewer

## The way the simulator works
1. we call search.py, it creates an instance of the parallel hillclimber
2. we evaluate the parents (do this step population size times)
    a. We run Run_Simulation()
    b. This calls the robot constructor with the specified ID
        c. Robot gets the sensor values and updates its neural network values to what is included in brainID.nndf
        d. The robot then acts based on the values given
        e. prints the fitness of that robot in a file
    f. We then create a copy of the parent and then mutate it
    g. after doing steps a-e again, we check if the children or parent had a better fitness and select the one that did

3. Run the entireity of step 2 Generationsize times




#### TO RUN ####
1. Switch to branch a6try4
2. Run 
```bash
python3 search.py
```

###  Credits ###
CS396 Artificial Life - Prof Sam Kriegman
LudoBots Tutorial - https://www.reddit.com/r/ludobots/
