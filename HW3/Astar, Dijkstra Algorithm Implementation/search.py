import heapq
import numpy as np
# Basic searching algorithms

# Class for each node in the grid
# First off, I didn't modify any FUNCTIONS, so this is a Class and if you have a problem with modifications,
# maybe change how the Class is set up.
class Node:
    def __init__(self, row, col, is_obs, h, g=None, cost=None, parent=None):
        self.row = row        # coordinate
        self.col = col        # coordinate
        self.is_obs = is_obs  # obstacle?
        self.g = g            # cost to come (previous g + moving cost)
        self.h = h            # heuristic
        self.cost = cost      # total cost (depend on the algorithm) Please note this is not what I would name it but
        # is what it was already called, this is the f = g + h
        self.parent = parent  # previous node

    def __lt__(self, other):
        # Custom comparison for heapq based on cost values
        return self.cost < other.cost

# The following two functions are helpers for both dijkstra and A*, both dijkstra and A* were written from scratch,
# so they are not duplicates of each other.
def get_neighbors(grid, node):
    '''
    Returns the neighbors of a grid that are reachable and are not obstacles

    arguments:
    grid - a np array of nodes for the grid itself
    noe  - the starting node we are looking for neighbors of

    return:
    neighbors - a list of Nodes that are neighbors of the node that are not obstacles
    '''
    neighbors = []
    r, c = grid.shape
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for dr, dc in dir:
        new_row, new_col = node.row + dr, node.col + dc
        if 0 <= new_row < r and 0 <= new_col < c:
            if not grid[new_row, new_col].is_obs:
                neighbors.append(grid[new_row, new_col])
    return neighbors


def nodeify(grid):
    '''
    Returns a np array of nodes. Using np since it is more efficient than list, and has helper functions

    args:
    grid - A nested list with datatype int. 0 represents free space while 1 is obstacle.
           e.g. a 3x3 2D map: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    return:
    node_graph - a np array of nodes, called a graph because why not.
    '''
    node_graph = np.empty([len(grid),len(grid[0])], dtype=Node)
    for r in range(0,len(grid)):
        for c in range(0,len(grid[r])):
            node_graph[r, c] = Node(r, c, grid[r][c], 0)
    return node_graph

def heuristicify(grid, goal):
    '''
    Returns a np array of nodes with updated heuristic cost depending on whatever the heuristic is defined as,
    eventually will be completely removed as it is inefficient, but since this homework only wants a heuristic that
    uses the manhattan distance, this is how I will be defining it. Why? great question.

    Please note I only have a separate class because I know I will be changing this code in the future to be more
    optimum, and to show none of my code is duplicated :/

    argument:
    grid - A nested list with datatype int. 0 represents free space while 1 is obstacle.
           e.g. a 3x3 2D map: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    goal - The goal node in the map. e.g. [2, 2]

    No need to return anything since it's just fixing up heuristics ._. Not a fan, but eh, I'm using the Node class
    '''
    rows, cols = grid.shape
    for r in range(0,rows):
        for c in range(0,cols):
            grid[r, c].h = abs(goal[0] - r) + abs(goal[1] - c)

def dijkstra(grid, start, goal):
    '''Return a path found by Dijkstra alogirhm 
       and the number of steps it takes to find it.

    arguments:
    grid - A nested list with datatype int. 0 represents free space while 1 is obstacle.
           e.g. a 3x3 2D map: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    start - The start node in the map. e.g. [0, 0]
    goal -  The goal node in the map. e.g. [2, 2]

    return:
    path -  A nested list that represents coordinates of each step (including start and goal node), 
            with data type int. e.g. [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]
    steps - Number of steps it takes to find the final solution, 
            i.e. the number of nodes visited before finding a path (including start and goal node)

    >>> from main import load_map
    >>> grid, start, goal = load_map('test_map.csv')
    >>> dij_path, dij_steps = dijkstra(grid, start, goal)
    It takes 10 steps to find a path using Dijkstra
    >>> dij_path
    [[0, 0], [1, 0], [2, 0], [3, 0], [3, 1]]
    '''
    np_grid = nodeify(grid)
    priority_q = [(0, np_grid[start[0], start[1]])]
    visited = set()
    np_grid[start[0], start[1]].g = 0
    np_grid[start[0], start[1]].cost = 0
    goal = np_grid[goal[0], goal[1]]
    steps = 0
    found = False
    path = []


    while priority_q:
        _, current_node = heapq.heappop(priority_q)
        steps = steps + 1
        if current_node in visited:
            continue # Skip the code and go to the next thing in the heap
        visited.add(current_node)

        if current_node == goal:
            while current_node: # While not none basically
                path.append([current_node.row, current_node.col])
                current_node = current_node.parent
            path.reverse()
            found = True
            break

        for neighbor in get_neighbors(np_grid, current_node):
            tentative_cost = current_node.g + 1 # Just 1, unless we are given map with edge weights .-.
            if neighbor.g is None or tentative_cost < neighbor.g:
                neighbor.g = current_node.g
                neighbor.cost = tentative_cost
                neighbor.parent = current_node
                heapq.heappush(priority_q, (tentative_cost, neighbor))

    if found:
        print(f"It takes {steps} steps to find a path using Dijkstra")
    else:
        print("No path found")
    return path, steps


def astar(grid, start, goal):
    '''Return a path found by A* alogirhm 
       and the number of steps it takes to find it.

    arguments:
    grid - A nested list with datatype int. 0 represents free space while 1 is obstacle.
           e.g. a 3x3 2D map: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    start - The start node in the map. e.g. [0, 0]
    goal -  The goal node in the map. e.g. [2, 2]

    return:
    path -  A nested list that represents coordinates of each step (including start and goal node), 
            with data type int. e.g. [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]
    steps - Number of steps it takes to find the final solution, 
            i.e. the number of nodes visited before finding a path (including start and goal node)

    >>> from main import load_map
    >>> grid, start, goal = load_map('test_map.csv')
    >>> astar_path, astar_steps = astar(grid, start, goal)
    It takes 7 steps to find a path using A*
    >>> astar_path
    [[0, 0], [1, 0], [2, 0], [3, 0], [3, 1]]
    '''
    np_grid = nodeify(grid)
    heuristicify(np_grid, goal)
    priority_q = [(0, np_grid[start[0], start[1]])]
    visited = set()
    np_grid[start[0], start[1]].g = 0
    np_grid[start[0], start[1]].cost = 0
    goal = np_grid[goal[0], goal[1]]
    steps = 0
    found = False
    path = []

    while priority_q:
        _, current_node = heapq.heappop(priority_q)
        steps = steps + 1
        if current_node in visited:
            continue  # Skip the code and go to the next thing in the heap
        visited.add(current_node)
        if current_node == goal or current_node.g == goal.g:
            current_node == goal # Here to solve the problem of goal found but multiple things with same g cost
            while current_node:  # While not none basically
                path.append([current_node.row, current_node.col])
                current_node = current_node.parent
            path.reverse()
            found = True
            break

        for neighbor in get_neighbors(np_grid, current_node):
            f = current_node.g + neighbor.h + 1 # Just the heuristic this time plus cost to move plus g
            if neighbor.g is None or f < neighbor.cost:
                neighbor.g = current_node.g + 1
                neighbor.cost = f
                neighbor.parent = current_node
                heapq.heappush(priority_q, (f, neighbor))

    if found:
        print(f"It takes {steps} steps to find a path using A*")
    else:
        print("No path found")
    return path, steps


# Doctest
if __name__ == "__main__":
    # load doc test
    from doctest import testmod, run_docstring_examples
    # Test all the functions
    testmod()
