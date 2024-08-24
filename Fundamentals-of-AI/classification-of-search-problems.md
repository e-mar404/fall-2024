# Search

---
### Reading 

**Artificial Intelligence: A Modern Approach**

    Ch. 3
    Ch. 4 (129-140)
    Ch. 5 (164-183)

---


## Classification of search problems, terminology and overview

Search problems get divided into 3 big categories:
1.  classical search problems
    - observable, deterministic, known environment
    - when the assumptions dont hold the problem becomes more complex

2. optimization problems
    - the solution matters, but how you get it doesn't

3. constraint satisfaction problems
    - the state is not a black box or indivisible, but it can be represented as a set of variables

### Classical Search Problem

**The 8-puzzle**

3*3 board with eight nums and a space
tile adj to blank space can move
State: specifies the location of the tiles and the blank space
Action: move blank space l, r, u, d
Goal: find a sequence of actions that leads from start state to a specified goal state

To solve this we can use a *global search* and make a tree of actions with bfs. The goal state will then be reached at some point on one of the leaf nodes.

### Optimization Problem

Need to find the best state given the objective, but it is not important how we got there. This means that only the final configuration is important.

An example of this is the 8-queens problem. We dont care in what order we put the queens or how we put them we just want the final location of all 8 queens.

Can be solved by using *local search* (only evaluate and modify the current sates, not systematically exploring paths from an initial state)

We can graph this with a given objective function `f(S)` that will evaluate the state `S`. Then the goal is to find the global maximum of ploting the values of `f(s)`.

### Constraint Satisfaction Problem

- each state can eb represented as a set of variables
- a problem is solved when each variable has a value that satisfiest any given constraints given
- constraints can significatly reduce the state search space by identifying the values that violate the constraints
- Ex: map coloring (coloring each region either red, blue, ro green in such a way that no neighboring regions have the same color)
