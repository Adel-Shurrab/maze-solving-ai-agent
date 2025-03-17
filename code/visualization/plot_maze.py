# code/visualization/plot_maze.py
from pyamaze import maze, agent, textLabel

def plot_maze(m, path, algorithm_name):
    """Visualize the maze and the solution path."""
    a = agent(m, footprints=True, filled=True)
    m.tracePath({a: path})
    textLabel(m, f'{algorithm_name} Path Length', len(path) + 1)
    m.run()