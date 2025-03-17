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

---

## Project Overview
This project demonstrates maze solving using informed and uninformed search algorithms. The implementation features:
- A* algorithm with Manhattan distance heuristic
- Breadth-First Search (BFS)
- Dynamic maze generation with customizable loops
- Path visualization with step-by-step animation

---

## Features
- **Search Algorithms**:  
  - **A***: Optimized with Manhattan distance heuristic  
  - **BFS**: Uninformed search guaranteeing shortest path  
- **Maze Generation**:  
  - Customizable grid sizes (up to 20x20)  
  - Adjustable loop percentage (0-100%)  
- **Visualization**:  
  - Real-time path tracing with `pyamaze`  
  - Path length comparison between algorithms  

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

The default configuration:

    Generates a 20x20 maze with 40% loops

    Solves using A* algorithm

    Displays solution path with agent animation

To modify behavior:

    Edit code/main.py:

        Change maze dimensions: rows, cols = 20, 20

        Adjust loop percentage: loopPercent=40

        Uncomment BFS section to compare algorithms

Example output:

    Interactive maze window with agent path

    Path length displayed in window title

---

## Team Members
- **Adel Surrab**: Algorithm Developer (A\*/BFS/DFS)
- **Abd Alhaleem**: Visualization Lead (matplotlib)
- **Faisal Alzeer**: Testing & Documentation

---

## Project Structure
```plaintext
maze-solving-ai-agent/  
├── code/  
│   ├── algorithms/             # A*, BFS, and DFS implementations  
│   ├── visualization/          # Maze plotting code  
│   ├── tests/                  # Unit tests  
│   └── main.py                 # Entry point  
├── data/                       # Maze files and results 
├── docs/                       # Report and presentation  
├── assets/                     # Images/icons  
├── .gitignore                  # Ignored files  
├── requirements.txt            # Python dependencies  
└── README.md                   # This file  
```
