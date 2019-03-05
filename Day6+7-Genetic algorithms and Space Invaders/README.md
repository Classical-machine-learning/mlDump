# README

- Based on Darwins survival of the fittest. 
- Natural selection principles.

## Phases
1) Initial Population
2) Fitness function
3) Selection
4) Crossover
5) Mutation

## Initial 
- Starts with population
- Parameters are defined as genes
- Rep as a string(Encoded binary values)

## Fitness 
- How fit an indiv is
- Provides a fitness score
- Probability of an individual to be selected for selection
- Metric

## Selection
- Select the fittest
- Pass their genes to the next stage
- Two pairs of individuals are selected based on their fitness score

## Crossover
- Most significant
- Random crossover point is chosen in the genes
- Offspring are created by exchanging the genes among the parents till the crossover point.
- Newly created offspring are added to the population

## Mutation
- In some offspring some genes are mutated
- Low random probability
- Some bits can be flipped
- To maintain diversity and prevent premature convergence

## Termination
- Stops when population does not produce offspring that are very different
- New generations keep forming with individuals with least fitness die.
- Space for new algorithms is provided

## Implementation is done in the following Repo
- https://github.com/SubhadityaMukherjee/Space-Invaders-Genetic-Algorithm

## Algorithm and most of the implementation sourced from 
https://github.com/llSourcell/Evolutionary_Space_Invaders/tree/master/python


