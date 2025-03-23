# Maze-Solving AI Agent 🧩

Welcome to the **Maze-Solving AI Agent** project! This Python-based project implements intelligent agents that solve mazes using search algorithms like **A*** and **BFS**. The agent navigates from the bottom-right corner to the top-left corner, with visualization powered by `pyamaze`.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
5. [Team Members](#team-members)
6. [Project Structure](#project-structure)
7. [Performance Metrics](#performance-metrics)

---

## Project Overview
This project demonstrates maze solving using informed and uninformed search algorithms. The implementation features:
- **A*** algorithm with Manhattan distance heuristic
- **BFS** (Breadth-First Search) for guaranteed shortest paths
- Dynamic maze generation with customizable loops
- Path visualization with step-by-step animation
- Performance metrics including execution time and nodes explored

---

## Features
- **Search Algorithms**:  
  - **A***: Optimized with Manhattan distance heuristic and priority queue  
  - **BFS**: Uninformed search using a standard queue, guaranteeing the shortest path  
- **Maze Generation**:  
  - Customizable grid sizes (up to 35x35)  
  - Adjustable loop percentage (0-100%)  
- **Visualization**:  
  - Real-time path tracing with `pyamaze`  
  - Path length comparison between algorithms  
  - Multiple paths visualized simultaneously (BFS in red, A* in blue)  
- **Performance Metrics**:  
  - Execution time for each algorithm  
  - Number of nodes explored  
  - Path length comparison  

---

## Setup Instructions
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/Adel-Shurrab/maze-solving-ai-agent.git
   cd maze-solving-ai-agent
   ```

2. **Install Dependencies**:  
   ```bash
   pip install pyamaze
   ```

3. **Run the Agent**:  
   ```bash
   python code/main.py
   ```

---

## Usage

### Default Configuration:
- Generates a **20x20 maze** with **10% loops**
- Solves using both **BFS** and **A*** algorithms
- Displays solution paths with agent animation
- Prints performance metrics (time and nodes explored)

### Customization:
Edit `code/main.py` to modify:
- Maze dimensions:  
  ```python
  rows, cols = 20, 20  # Change to desired size
  ```
- Loop percentage:  
  ```python
  loopPercent = 10  # Adjust between 0 (no loops) and 100 (many loops)
  ```
- Visualization:  
  Uncomment/comment sections in `main.py` to enable/disable specific algorithms.

### Example Output:
```plaintext
=== Performance Metrics ===
BFS Time: 0.0019s | Nodes Explored: 1226
A* Time: 0.0064s | Nodes Explored: 1303

Path Lengths - BFS: 90 | A*: 90
```

---

## Team Members
- **Adel Shurrab**
- **Abd Alhalim**
- **Faisal Alzeer**

---

## Project Structure
```plaintext
maze-solving-ai-agent/  
├── code/  
│   ├── algorithms/             # A* and BFS implementations  
│   │   ├── a_star.py           # A* with priority queue  
│   │   └── bfs.py              # BFS with standard queue  
│   ├── visualization/          # Maze plotting code  
│   │   ├── maze_generator.py   # Maze generation logic  
│   │   └── plotter.py          # Path visualization  
│   └── main.py                 # Entry point  
├── data/                       # Maze files and results 
├── docs/                       # Report and presentation  
├── assets/                     # Images/icons  
├── .gitignore                  # Ignored files  
├── requirements.txt            # Python dependencies  
└── README.md                   # This file  
```

---

## Performance Metrics
The project provides detailed performance metrics for each algorithm:
- **Execution Time**: Measures how long each algorithm takes to solve the maze.
- **Nodes Explored**: Counts the number of nodes explored during the search.
- **Path Length**: Compares the length of the paths found by BFS and A*.

### Example Output:
```plaintext
=== Performance Metrics ===
BFS Time: 0.0019s | Nodes Explored: 1226
A* Time: 0.0064s | Nodes Explored: 1303

Path Lengths - BFS: 90 | A*: 90
```

---

## Future Work
1. **Algorithm Extensions**:
   - Implement **Dijkstra’s Algorithm** for weighted grids.
   - Add **bidirectional BFS** for memory optimization.
2. **Enhanced Heuristics**:
   - Experiment with **Euclidean distance** or machine learning-based heuristics.
3. **Real-World Integration**:
   - Deploy on robotics platforms (e.g., ROS) for physical maze-solving.
4. **Interactive Features**:
   - Let users design custom mazes via a GUI.