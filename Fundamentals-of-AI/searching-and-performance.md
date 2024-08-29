# Searching for soltions

Solution is a sequence of actions. These sequences are usially represented with a search tree.

The possible action sequences start from the initial state (root of tree). The branches of the tree correspoind to sequences of actions and nodes correspond to states.

The variation of search algorithms doesnt't come from their structure it come from the variation on the search strategy (how to choose which state to expand next).

### Avoiding Looping & Repated States

Tree search vs Graph search
- graph search removed the redundant paths by introducing the explored set to remember the expanded nodes. (visited[])

Different search algos handle the queueing of the enxt element to expand in different ways. Some different orders are: FIFO, LIFO and Priority Queue.

### Performance Measure

Four elements of performance:
- completeness
- optimality
- time complexity
- space complexity

Parameters for the copmlexity:
- branching factor
- depth fo shallowest goal node
- moximum length of any path in the state space
