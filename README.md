# Flapi Birb
**Implementing the Legendary game, Flappy Bird using the NEAT(Neuroevolution of augmenting topologies) algorithm.**

## The Game:
- Run the main.sh script:
    - Note: installs: `neat-python` and `pygame` using `pip`

- There are two options to Play the game: 
    - Play the game yourself
    - Let the NEAT Algorithm play it for you

## The Algorithm
NEAT is a genetic algorithm, which evolves different structures for the neural network. There are some initial species, and those who live the longest have the highest score. Thus passing on thier "genes", which is basically their network. Some mutations and and some cross-overs create the Next-Gen NN.

These networks start out simple, and for a game such as this, do not require many generations to get god-level at it. (Of course, given enough population size to begin with.)

### References
- [The NEAT Algorithm Paper](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf)
- The implementation of the NEAT algorithm is taken from [here](https://github.com/CodeReclaimers/neat-python) 