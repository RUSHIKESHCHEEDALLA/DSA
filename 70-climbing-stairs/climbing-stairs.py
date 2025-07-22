class Solution(object):
    def climbStairs(self, n):
        dp=[-1 for _ in range(n+1)]
        def fa(n,dp):
            if n<=3:
                return n
            if dp[n]!=-1:
                return dp[n]
            dp[n]=fa(n-1,dp)+fa(n-2,dp)
            return dp[n]
        return fa(n,dp)
        
            
        