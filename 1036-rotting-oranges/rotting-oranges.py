import numpy as np
class Solution(object):
    def orangesRotting(self, grid):
        l=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2 :l.append([i,j])
        print(l)
        va = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        c=0
        def bfs(l):
            q=[]
            d= [(0,-1),(-1,0),(1,0), (0,1)]
            while l:
                r,c=l.pop(0)
                va[r][c]=1
                for x,y in d:
                    nr=r+x
                    nc=c+y
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1 :
                        grid[nr][nc]=2
                        q.append([nr,nc])
            return q
        while l:
            l=bfs(l)
            if l:
                c+=1
        print(grid)
        

        flattened = list(np.array(grid).flatten())
        
        return -1 if 1 in flattened else c

        