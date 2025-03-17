# code/visualization/plot_maze.py
from pyamaze import maze, agent, textLabel

def plot_maze(m, path, algorithm_name):
    """
    Visualize the maze and the solution path.

    Parameters:
    m (maze): The maze object.
    path (dict): The solution path as a dictionary of cell connections.
    algorithm_name (str): The name of the algorithm used to solve the maze.
    """
    a = agent(m, footprints=True, filled=True)
    m.tracePath({a: path})
    textLabel(m, f'{algorithm_name} Path Length', len(path) + 1)
    m.run()