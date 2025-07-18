class Solution(object):
    def updateMatrix(self, mat):

        va=[[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        q=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0 and va[i][j]==0:
                    q.append([i,j,0])
                    mat[i][j]=0
                    va[i][j]=1

        while q:
            r,c,v=q.pop(0)
            d=[(0,1),(0,-1),(-1,0),(1,0)]
            for x,y in d:
                nr=r+x
                nc=c+y
                if 0<=nr<len(mat) and 0<=nc<len(mat[0]) and mat[nr][nc]==1 and va[nr][nc]==0:
                    mat[nr][nc]=v+1
                    va[nr][nc]=1
                    q.append([nr,nc,v+1])  
                              
        return mat

        