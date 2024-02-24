# Dijkstra's and A* Pathfinding Algorithms

## Code and Algorithm Explanation

### Dijkstra's Algorithm
Dijkstra's algorithm graph traversal algorithm that finds the shortest path from a start node to all other nodes in a weighted graph. It works by maintaining a priority queue of nodes to explore starting with the start node. It iteratively selects the node with the lowest cost to reach and explores its neighbors, updating their costs if a shorter path is found. Dijkstra's algorithm guarantees the shortest path for non-negative edge weights.

**Pseudocode**:

Initialize distance array for all nodes to infinity, or None in my case
Set distance of start node to 0

While priority queue is not empty:
CurrentNode = node with the lowest distance from the priority queue
If CurrentNode is the goal node, break
For each neighbor of CurrentNode:
Calculate distance
If distance < distance[neighbor]:
Update distance[neighbor]
Add neighbor to priority queue


### A* Algorithm
A* is an informed search algorithm that combines elements of Dijkstra's algorithm and heuristics. It estimates the total cost from the start node to the goal node by considering both the cost to reach the node (g) and a heuristic estimate of the remaining cost (h). A* selects nodes to explore based on their total cost, prioritizing nodes that are likely to lead to the goal. It is guaranteed to find the shortest path if the heuristic is admissible.

**Pseudocode**:

Add start node to priority queue with distance 0
Initialize visited list as empty
Initialize heuristics since we are using manhattan

While open list is not empty:
CurrentNode = node with the lowest f = g + h value from priority queue
Add CurrentNode to visited list
If CurrentNode is the goal node, break
For each neighbor of CurrentNode:
Calculate f
If f < f[neighbor]:
Update f[neighbor]
Add neighbor to priority queue


## Test Result, and Explanation
- Dijkstra's algorithm explores all nodes uniformly, considering only the cost to reach each node. It guarantees the shortest path but may take more steps if a heuristic (if any) is not considered.
- A* algorithm considers both the cost to reach a node and an estimate of the remaining cost to the goal (heuristic). It prioritizes nodes that appear promising based on the heuristic. A* is often faster than Dijkstra's when the heuristic is well-chosen and admissible.
- The reason different algorithms gives different results is that A* can be more efficient in finding the optimal path when using a good heuristic. Dijkstra's is a more general approach that can handle scenarios where a heuristic is not defined.
- The choice of heuristic can impact the efficiency of A*; a better heuristic usually leads to faster pathfinding. Different maps may yield different results depending on the presence of obstacles and the locations of the start and goal.
