# code/algorithms/bfs.py
from pyamaze import maze

def BFS(m):
    """
    BFS implementation using standard FIFO queue
    Returns path and nodes explored count
    """
    start = (m.rows, m.cols)
    goal = (1, 1)
    
    # Standard queue implementation
    frontier = [start]
    explored = {start: None}
    nodes_explored = 0

    while frontier:
        currCell = frontier.pop(0)  # FIFO operation
        nodes_explored += 1
        
        if currCell == goal:
            break
        
        # Check all directions
        for d in 'ESNW':
            if m.maze_map[currCell][d]:
                x, y = currCell
                # Calculate child cell
                if d == 'E':
                    child = (x, y+1)
                elif d == 'W':
                    child = (x, y-1)
                elif d == 'N':
                    child = (x-1, y)
                elif d == 'S':
                    child = (x+1, y)

                if child not in explored:
                    frontier.append(child)
                    explored[child] = currCell

    # Reconstruct path
    path = {}
    cell = goal
    while cell != start:
        path[explored[cell]] = cell
        cell = explored[cell]
    
    return path, nodes_explored