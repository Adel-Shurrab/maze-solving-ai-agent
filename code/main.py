from algorithms.bfs import BFS
from algorithms.a_star import aStar
from visualization.maze_generator import generate_maze
from visualization.plotter import MazePlotter
from pyamaze import COLOR
import time

def benchmark(func, maze):
    """benchmarking with process time"""
    start = time.process_time()
    path, nodes = func(maze)
    elapsed = time.process_time() - start
    return path, elapsed, nodes

def main():
    # Generate maze with validation
    try:
        m = generate_maze(20, 20, loopPercent=40)
        if not m.maze_map:
            raise ValueError("Maze generation failed")
    except Exception as e:
        print(f"Maze Error: {e}")
        return

    # Benchmark algorithms
    try:
        bfs_path, bfs_time, bfs_nodes = benchmark(BFS, m)
        astar_path, astar_time, astar_nodes = benchmark(aStar, m)
    except KeyError as e:
        print(f"Pathfinding Error: Missing key {e}")
        return

    # Results analysis
    print("\n=== Performance Metrics ===")
    print(f"BFS Time: {bfs_time:.6f}s | Nodes Explored: {bfs_nodes}")
    print(f"A* Time: {astar_time:.6f}s | Nodes Explored: {astar_nodes}")
    print(f"\nPath Lengths - BFS: {len(bfs_path)} | A*: {len(astar_path)}")
    
    # Visualization
    try:
        plotter = MazePlotter(m)
        plotter.add_path(bfs_path, COLOR.red, "BFS")
        plotter.add_path(astar_path, COLOR.blue, "A*")
        plotter.show()
    except Exception as e:
        print(f"Visualization Error: {e}")

if __name__ == "__main__":
    main()