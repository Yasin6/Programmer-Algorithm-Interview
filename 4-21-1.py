# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:26:33 2018

@author: Administrator
"""

class  Maze:
    def  __init__(self): 
        self.N= 4
    # 打印从起点到终点的路线 
    def  printSolution(self,sol):
        i=0
        while  i<self.N:
            j=0
            while  j < self.N:
                print  sol[i][j],
                j +=1
            print  '\n'
            i +=1      
    # 判断x和y是否是一个合理的单元 
    def  isSafe(self,maze,x,y):
        return  x >= 0 and x < self.N and y >= 0 and \
                y < self.N and maze[x][y] == 1
    """
    使用回溯的方法找到一条从左上角到右下角的路径
    maze表示迷宫, x、y表示起点，sol存储结果
    """
    def  getPath(self,maze,x,y,sol):
        # 到达目的地 
        if  x == self.N - 1 and y == self.N - 1:
            sol[x][y] = 1
            return  True       
        # 判断maze[x][y]是否是一个可走的单元 
        if  self.isSafe(maze, x, y):
            # 标记当前单元为1 
            sol[x][y] = 1
            # 向右走一步 
            if  self.getPath(maze, x + 1, y, sol):
                return  True
            # 向下走一步 
            if  self.getPath(maze, x, y + 1, sol):
                return  True
            # 标记当前单元为0用来表示这条路不可行，然后回溯 
            sol[x][y] = 0
            return  False
        return  False

if  __name__=="__main__":
    rat =Maze()
    maze=[[1, 0, 0, 0],
          [1, 1, 0, 1],
          [0, 1, 0, 0],
          [1, 1, 1, 1]]
    sol=[[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    if   not rat.getPath(maze, 0, 0, sol):
        print  "不存在可达的路径"
    else:
        rat.printSolution(sol)

