class Solution(object):
    def isBipartite(self, graph):
        def bfs(i):
            va=[1 for _ in range(len(graph))]
            q=[i]
            va[i]=0
            while q:
                p=q.pop()
                l=graph[p]
                
                for i in l:
                    if va[i]==1:
                        va[i] = ~va[p]
                        q.append(i)
                    elif va[i]==va[p]:
                        return False
            return True
        for i in range(len(graph)):
            if bfs(i)==False:
                return False

        return True
            
       




        

        