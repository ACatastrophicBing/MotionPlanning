# RBE 550 Assignment 1 Turn-In Doc

# How BFS works : 
Breadth-First Search (BFS) is a graph traversal algorithm used to explore nodes in a graph or tree in a forward motion. It starts from an arbitrary node or "root" and explores all the neighbor nodes at the present depth before moving on to nodes at the next depth level. It is commonly used to find the shortest path from a source node to a destination node in unweighted graphs. It can be used to create topological maps for graphs.
# BFS Pseudocode : 
1. Create an empty queue and queue the starting node with a depth of 0.
2. Create a set to keep track of visited nodes.
3. While the queue is not empty:
     - Dequeue a node from the queue.
     - If the dequeued node is the goal node, return the solution.
     - If the dequeued node has not been visited:
         - Mark the node as visited.
         - Queue all unvisited neighbor nodes of the current node with an incremented depth.
4. If the queue becomes empty and the goal node is not found, there is no path to the goal node.

# How DFS works : 
Depth-First Search (DFS) is a graph traversal algorithm used to explore nodes in a graph or tree by visiting as far down a branch as possible before backtracking. It starts from the an arbitrary node or "root" and explores as far as possible along each branch before backtracking to explore other branches. Can be written recursively, but this assignment setup didn't allow for such functionality.
# DFS Pseudocode :
1. Create an empty stack and push the starting node onto it.
2. Create a set to keep track of visited nodes.
3. While the stack is not empty:
     - Pop a node from the stack.
     - If the popped node is the goal node, return the solution.
     - If the popped node has not been visited:
         - Mark the node as visited.
         - For each unvisited neighbor node of the current node:
             - Push the neighbor node onto the stack.
4. If the stack becomes empty and the goal node is not found, there is no path to the goal node.

# Testing : 
By running `python main.py`, both DFS and BFS follow properly following the right, down, left, up order for visiting new nodes. No new map was needed to be created as you can follow proof of this with the provided maps for both BFS and DFS.

# Reference Paper / Resources : 
None.