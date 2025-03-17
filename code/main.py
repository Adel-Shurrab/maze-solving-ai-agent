# code/main.py
from algorithms.a_star import aStar
from algorithms.bfs import BFS
from visualization.maze_generator import generate_maze
from visualization.plot_maze import plot_maze

def main():
    # Generate a maze
    rows, cols = 15, 15
    maze = generate_maze(rows, cols, loopPercent=40)

    # Solve using A*
    a_star_path = aStar(maze)
    plot_maze(maze, a_star_path, "A*")

    # Solve using BFS
    bfs_path = BFS(maze)
    plot_maze(maze, bfs_path, "BFS")

if __name__ == "__main__":
    main()