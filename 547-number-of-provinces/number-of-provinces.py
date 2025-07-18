class Solution(object):
    def findCircleNum(self, isConnected):
        def dfs(node,va,isConnected):
            va[node]=1
            l=isConnected[node]
            for i in range(len(l)):
                if l[i]==1 and va[i]==0:
                    dfs(i,va,isConnected)
        c=0
        va=[0]*len(isConnected)
        for i in range(len(va)):
            if va[i]==0:
                c+=1
                dfs(i,va,isConnected)
        return c

        