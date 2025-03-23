from pyamaze import maze

def generate_maze(rows, cols, loopPercent=0):
    """Robust maze generator with validation"""
    try:
        if rows < 2 or cols < 2:
            raise ValueError("Maze dimensions must be at least 2x2")
            
        m = maze(rows, cols)
        m.CreateMaze(loopPercent=loopPercent)
        
        if not m.maze_map or len(m.maze_map) < rows*cols:
            raise RuntimeError("Maze generation incomplete")
            
        return m
    except Exception as e:
        print(f"Maze Generation Error: {e}")
        raise