from pyamaze import agent, COLOR, textLabel

class MazePlotter:
    def __init__(self, maze):
        self.maze = maze
        self.agents = []
        self.labels = []
        
    def add_path(self, path, color, label):
        """Add a path with visualization"""
        a = agent(self.maze, footprints=True, color=color, shape='square', filled=True)
        self.maze.tracePath({a: path})
        self.labels.append(textLabel(self.maze, f"{label} Path Length", len(path)+1))
        self.agents.append(a)
        
    def show(self):
        """Display the visualization"""
        self.maze.run()