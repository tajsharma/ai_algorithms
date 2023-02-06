from pyamaze import maze 
from queue import PriorityQueue

def h(cell1,cell2):#calculates the heuristic value using manhattan distance equation
    x1,y1 = cell1
    x2,y2 = cell2 

def aStar(maze):
    start = (maze.rows,maze.cols)
    g_score = {cell:float('inf') for cell in maze.grid}#sets g value for all nodes to inf at first bc we havent visited them yet
    g_score[start] = 0 #gscore of starting val will be 0
    f_score = {cell:float('inf') for cell in maze.grid}
    f_score[start] = h(start,(1,1)) #f score from the start will be 0 + h(start to end) value 

worldMap = maze(6,6)
worldMap.CreateMaze()

worldMap.run()