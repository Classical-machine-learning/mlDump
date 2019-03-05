# README

## Markov Chains

- Mathematical system defined as a collection of random variables
- Transition between stares according to probabilistic rules
- Not dependent on the preceding state : Memoryless

## Use 

- Game theory
- Economics
- Comm theory
- Genetics
- Finance
- Cruise control
- PageRank
- Reddit

## Markov Chain
- Random process with the Markov property
- Stochastic propery : Collection of random variables
- Discrete TIme (most cases). DTMC: Discrete Time Markov Chain

## Discrete Time Markov Chain
- System is in a certain state at each step
- State randomly changes in between steps
- The probability of moving to the next state only depends on the present state.
(NOTE: <> is subscript)

P(X<n+1>=x|X<1>=x<1>,X<2>=x<2>,...,X<n>)=P(X<n+1>=x|X<n>=x<n>)
- POssible values of X form a state space

## Model
- Probablistic Automaton
- Transition Matrix
- Matrix js Stochastic 

## Properties of Markov Chains
- Reducibility: Irreducible if any state from any state
- Periodicity: If chain can return to the state only as multiples of some integer>1
- Transience: If we start at state i, there is a non zero prob of never returning to i.
- Recurrent: Positive recurrent if expected to return within a finite no of steps or null recurrent otherwise.
- Ergodicity: If not periodic as well as positive recurrent. If all states in an irreducible Markov chain are ergodic: Chain is also ergodic
- Absorbing State: if it is impossible to leave this state.

