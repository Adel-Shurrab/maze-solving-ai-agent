# code/visualization/maze_generator.py
from pyamaze import maze

def generate_maze(rows, cols, loopPercent=0):
    """
    Generate a maze using pyamaze.

    Parameters:
    rows (int): Number of rows in the maze.
    cols (int): Number of columns in the maze.
    loopPercent (int, optional): Percentage of loops in the maze. Defaults to 0.

    Returns:
    maze: The generated maze object.
    """
    m = maze(rows, cols)
    m.CreateMaze(loopPercent=loopPercent,saveMaze=True,loadMaze=None)
    return m