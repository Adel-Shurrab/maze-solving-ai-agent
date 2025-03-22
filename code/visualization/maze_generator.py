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
    m.CreateMaze(loopPercent=loopPercent, loadMaze='maze--2025-03-22--17-09-11.csv')
    return m