class Solution(object):
    def setZeroes(self, matrix):
        c=[]
        r=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    # print(i)
                    # print(j)
                    r.append(i)
                    c.append(j)
        for i in range(len(matrix)):
            if i in r:
                for j in range(len(matrix[i])):
                    matrix[i][j]=0
        # print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j in c:
                    matrix[i][j]=0
        # print(matrix)
        
        