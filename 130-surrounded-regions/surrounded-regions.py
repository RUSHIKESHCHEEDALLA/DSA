class Solution(object):
    def solve(self, board):
        def bfs(i,j,va,board):
            q=[[i,j]]
            va[i][j]=1
            while q:
                r,c=q.pop(0)
                d=[(0,1),(0,-1),(1,0),(-1,0)]
                for x,y in d:
                    nr=r+x
                    nc=c+y
                    if 0<=nr<len(board) and 0<=nc<len(board[0]) and va[nr][nc]==0 and board[nr][nc]=="O":
                        va[nr][nc]=1
                        q.append([nr,nc])

        va=[[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        r=len(board)
        c=len(board[0])
        dr=[0,r-1]
        dc=[0,c-1]
        for i in range(r):
            if i in dr:
                for j in range(c):
                    if board[i][j]=="O" and va[i][j]==0:
                        bfs(i,j,va,board)
            else:
                for j in dc:
                    if board[i][j]=="O" and va[i][j]==0:
                        bfs(i,j,va,board)
        for i in range(r):
            for j in range(c):
                if board[i][j]=="O" and va[i][j]==0:
                    board[i][j]="X"
        


        