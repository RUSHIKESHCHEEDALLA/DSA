class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        else:
            dp=[-1 for _ in range(rowIndex+1)]
            dp[0]=[1]
            dp[1]=[1,1]
            for i in range(2,rowIndex+1):
                l=dp[i-1]
                ans=[1]
                if l!=-1:
                    for  j in range(1,len(l)):
                        ans.append(l[j-1]+l[j])
                    ans.append(1)
                    dp[i]=ans
            return dp[rowIndex]
                    
                

            