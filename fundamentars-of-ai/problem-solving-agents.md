# Problem Solving Agents

## Purpose
- find a sequence of actions that achieve a clear goal

### Steps
1. make goal
2. chose a state space and action space
3. search
4. execute found solution

Ex.

A weighted graph of places that can be traveled by train. 

Goal: reach Bucharest within the cost restraint.
    - goal `state = In(Bucharest)`

Problem Faundation: decide what actions and states it should consider 
    - action: driving from one town to the another
    - state: being in another town

1.
    a) Initial state: starting town
    b) State space: the set of all reachable states by any sequence of actions from the initial state

2. Action space: the set of all possible actions the agent can take

3. Transition model: returns the next state `s'` that results from taking action `a` in current state `s`
    eg. `RESULT(state=In(town11), Go(town2)) = In(town2)`

4. Goal test: check if a given state is a goal state
    eg. `check if in current_state = In(goal_town)`

5. Path cost: a numeric coast for a path
    Step cost: cost of current state `s` and taking an action `a`
    Path cost: sum of step costs along the path


## Classical Problems
*Real world problems*
- route finding
- traveling salesperson
- robot navigation
- automatic assembly sequencing
- protein design
