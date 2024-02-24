from collections import deque

# Basic searching algorithms

# Class for each node in the grid
class Node:
    def __init__(self, row, col, is_obs, parent = None, cost = None):
        self.row = row        # coordinate
        self.col = col        # coordinate
        self.is_obs = is_obs  # obstacle?
        self.cost = cost      # total cost (depend on the algorithm)
        self.parent = parent    # previous node


def bfs(grid, start, goal):
    '''Return a path found by BFS alogirhm 
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
    >>> bfs_path, bfs_steps = bfs(grid, start, goal)
    It takes 10 steps to find a path using BFS
    >>> bfs_path
    [[0, 0], [1, 0], [2, 0], [3, 0], [3, 1]]
    '''
    # Define possible moves: up, down, left, right
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Get the dimensions of the grid
    rows, cols = len(grid), len(grid[0])

    # Initialize a visited set to keep track of visited nodes since we will never backtrack them
    visited = set()

    # Initialize a queue for BFS with the start node and its distance (step count)
    start_node = Node(start[0], start[1], False)
    goal_node = Node(goal[0], goal[1], False)
    queue = deque([(start_node, 0)])
    poorly_named_steps_for_assignment = 0

    while len(queue) > 0:
        poorly_named_steps_for_assignment = poorly_named_steps_for_assignment + 1
        (current_node, steps) = queue.popleft()

        # Check if the current_node is the goal node
        if current_node.row == goal_node.row and current_node.col == goal_node.col:
            found = True
            # Reconstruct the path from the goal to the start
            path = []
            while current_node != start_node:
                path.append([current_node.row, current_node.col])
                current_node = current_node.parent
            path.append([start_node.row, start_node.col])
            path.reverse()
            break

        # Explore neighboring nodes
        for move in moves:
            next_row, next_col = current_node.row + move[0], current_node.col + move[1]

            # Check if the next_node is within the grid and not an obstacle, and if it hasn't been visited yet
            if (0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 0 and (next_row, next_col)
                    not in visited):
                next_node = Node(next_row, next_col, False, parent=current_node)
                # Mark the next_node as visited
                visited.add((next_node.row, next_node.col))
                # Add the next_node to the queue with the updated steps count
                queue.append((next_node, steps + 1))
                if next_row == goal_node.row and next_col == goal_node.col:
                    queue.appendleft((next_node, steps + 1))
    if found:
        print(f"It takes {poorly_named_steps_for_assignment} steps to find a path using BFS")
    else:
        print("No path found")
    return path, poorly_named_steps_for_assignment


def dfs(grid, start, goal):
    '''Return a path found by DFS alogirhm 
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
    >>> dfs_path, dfs_steps = dfs(grid, start, goal)
    It takes 9 steps to find a path using DFS
    >>> dfs_path
    [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 3], [3, 3], [3, 2], [3, 1]]
    '''
    # Define possible moves: right, down, left, up, but flipped since that's how we are forced to use the queue here :(
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    # Get the dimensions of the grid
    rows, cols = len(grid), len(grid[0])

    # Initialize a visited set to keep track of visited nodes
    visited = set()

    # Initialize a queue for BFS with the start node and its distance (step count)
    start_node = Node(start[0], start[1], False)
    goal_node = Node(goal[0], goal[1], False)
    queue = deque([(start_node, 1)])
    poorly_named_steps_for_assignment = 0

    while len(queue) > 0:
        while True:
            (current_node, steps) = queue.pop()
            if (current_node.row, current_node.col) not in visited:
                break
        # Mark the next_node as visited
        visited.add((current_node.row, current_node.col))
        # Increment the number of "steps" which is actually just the number of nodes visited so it should be a
        # different word but whatever
        poorly_named_steps_for_assignment = poorly_named_steps_for_assignment + 1

        # Check if the current_node is the goal node
        if current_node.row == goal_node.row and current_node.col == goal_node.col:
            found = True
            # Reconstruct the path from the goal to the start
            path = []
            while current_node != start_node:
                path.append([current_node.row, current_node.col])
                current_node = current_node.parent
            path.append([start_node.row, start_node.col])
            path.reverse()
            break

        # Explore neighboring nodes
        for move in moves:
            next_row, next_col = current_node.row + move[0], current_node.col + move[1]

            # Check if the next_node is within the grid and not an obstacle, and if it hasn't been visited yet
            if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 0 and (
            next_row, next_col) not in visited:
                next_node = Node(next_row, next_col, False, parent=current_node)
                # Add the next_node to the queue with the updated steps count
                queue.append((next_node, steps + 1))
                if next_row == goal_node.row and next_col == goal_node.col:
                    queue.appendleft((next_node, steps + 1))
    if found:
        print(f"It takes {poorly_named_steps_for_assignment} steps to find a path using DFS")
    else:
        print("No path found")
    return path, poorly_named_steps_for_assignment


# Doctest
if __name__ == "__main__":
    # load doc test
    from doctest import testmod, run_docstring_examples
    # Test all the functions
    testmod()
