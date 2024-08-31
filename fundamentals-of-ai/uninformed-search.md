# Uninformed Search

Generate successors and distinguidh a goal state from a non-goal state.

Search strategies differ in the order in which nodes are expanded.

## Breath-first search

Search tree is expanded on a level by level order. SO first the root, then it checks the entire second level, then the third, and so on and so forth.

*Properties*:
- complete if and are finite
- optimal if all actions have the same cost
- time complexity and space copmlexity is both `O(V + E)`. `V` being the number of vertices and `E` the number of edges.

## Uniform-cost Search


