# code/algorithms/bfs.py
from pyamaze import maze, agent, COLOR, textLabel

def BFS(m):
    """
    BFS algorithm implementation for maze solving.

    Parameters:
    m (maze): The maze object.

    Returns:
    dict: The solution path as a dictionary of cell connections.
    """
    start = (m.rows, m.cols)
    frontier = [start]
    explored = [start]
    bfsPath = {}

    while len(frontier) > 0:
        currCell = frontier.pop(0)
        if currCell == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell

    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]

    return fwdPath