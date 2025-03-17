# code/algorithms/maze_generator.py
from pyamaze import maze

def generate_maze(rows, cols, loopPercent=0):
    """Generate a maze using pyamaze."""
    m = maze(rows, cols)
    m.CreateMaze(loopPercent=loopPercent)
    return m