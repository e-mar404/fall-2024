# Informed (Heuristic) Search

## Overview

Informed Search strategies use problem-specific knowledge beyond the problem definition itself. They can find solutions more efficiently than uninformed search strategies.

*What are heuristics*:
- rule of thumb, intuition
- a quick way to estimate how close is a state to the goal

## Best-first Search

- select node based on evaluation function (determine best course of action based on path cost, node, current state, goal, etc. This is unique to each situation)

Two popular BFS search strategies are:
- Greedy best-first search
- A* search

## Greedy Best-first Search

- almost the same as a regular best-first search but you expand the node that appears to be closes to the goal
- uses local optimization so it does not take into account the path cost required to get to the current state which might yield a bad solution
- a lot of cs algos are greedy
- there is no backtracking so if there is a bad decision (base on wtv local criteria), the algo will not revise the decision
- generally fast making it a go to for NP hard problems

## A* search

- aims to blind spots of local optimization and taking into account the path cost to get to the local state
- minimize the total estimated solution cost
- avoid expanding paths that are already expensive 

${ f(n) = g(n) + h(n) }

// g(n) being the path cost from root to node
// h(n) being the estimated cost of cheapest path from node to goal

### Optimality of A* Search

**Theorem 1.** The tree-search version of A* is optimal if it is *admissible*
**Theorem 2.** The graph-search version of A* is optimal if it is *consistent*


## Questions for later:
- what is heuristic search

