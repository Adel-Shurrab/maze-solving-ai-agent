# Maze-Solving AI Agent 🧩

Welcome to the **Maze-Solving AI Agent** project! This Python-based project implements intelligent agents that solve mazes using search algorithms like **A*** and **BFS**. The agent navigates from the start (`S`) to the goal (`G`) while avoiding walls (`#`), and the process is visualized using `matplotlib`.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#Usage)
5. [Team Members](#team-members)
6. [Project Structure](#project-structure)

---

## Project Overview
This project is part of the **Artificial Intelligence** course. The goal is to build an AI agent that solves mazes using search algorithms. The agent demonstrates rational decision-making by finding the shortest path from start to goal while avoiding obstacles.

---

## Features
- **Search Algorithms**:  
  - **A***: Optimized with Manhattan distance heuristic.  
  - **BFS**: Guarantees the shortest path (uninformed search).  
- **Visualization**:  
  - Animated maze-solving process using `matplotlib`.  
- **Custom Mazes**:  
  - Load mazes from text files or generate them dynamically.  
- **Performance Metrics**:  
  - Measure execution time and path length for comparison. 

---

## Setup Instructions
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/your-username/maze-solving-ai-agent.git
   cd maze-solving-ai-agent

2. **Install Dependencies**:
    pip install -r requirements.txt

3. **Run the Agent**:
    python code/main.py --maze data/mazes/simple_maze.txt
  
## Usage
**Running the Agent**
To solve a maze using **A***:
python code/main.py --maze data/mazes/simple_maze.txt --algorithm a_star

To solve a maze using **BFS**:
python code/main.py --maze data/mazes/simple_maze.txt --algorithm bfs

**Custom Mazes**
Add your own maze to data/mazes/ in the following format:
'''bash
S # #   #
  #   # #
    #   G

## Team Members
**Adel Surrab:** Algorithm Developer (A*/BFS).
**Abd Alhaleem:** Visualization Lead (matplotlib).
**Faisal Alzeer:** Testing & Documentation.

## Project Structure
maze-solving-ai-agent/  
├── code/  
│   ├── algorithms/             # A* and BFS implementations  
│   ├── visualization/          # Maze plotting code  
│   ├── tests/                  # Unit tests  
│   └── main.py                 # Entry point  
├── data/                       # Maze files and results 
├── docs/                       # Report and presentation  
├── assets/                     # Images/icons  
├── .gitignore                  # Ignored files  
├── requirements.txt            # Python dependencies  
└── README.md                   # This file  
