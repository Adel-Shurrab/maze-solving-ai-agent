# code/algorithms/a_star.py
from queue import PriorityQueue
from pyamaze import maze

def h(cell1, cell2):
    """Manhattan distance heuristic"""
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

def aStar(m):
    """
    A* implementation using PriorityQueue
    Returns path and nodes explored count
    """
    start = (m.rows, m.cols)
    goal = (1, 1)
    
    # Priority queue initialization
    open = PriorityQueue()
    open.put((h(start, goal), h(start, goal), start))
    
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0
    came_from = {}
    nodes_explored = 0

    while not open.empty():
        current = open.get()[2]  # Get cell from priority queue
        nodes_explored += 1
        
        if current == goal:
            break
            
        # Explore neighbors
        for d in 'ESNW':
            if m.maze_map[current][d]:
                x, y = current
                # Calculate child cell
                if d == 'E':
                    child = (x, y+1)
                elif d == 'W':
                    child = (x, y-1)
                elif d == 'N':
                    child = (x-1, y)
                elif d == 'S':
                    child = (x+1, y)

                # Update scores
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(child, float('inf')):
                    g_score[child] = tentative_g
                    f_score = tentative_g + h(child, goal)
                    open.put((f_score, h(child, goal), child))
                    came_from[child] = current

    # Reconstruct path
    path = {}
    cell = goal
    while cell != start:
        path[came_from[cell]] = cell
        cell = came_from[cell]
    
    return path, nodes_explored