class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        dp=[-1 for _ in range(len(cost))]
        dp[0]=cost[0]
        dp[1]=cost[1]
        for ind in range(2,len(cost)):
            dp[ind]=cost[ind]+min(dp[ind-1],dp[ind-2])
        print(cost)
        print(dp)
        return dp[len(cost)-1]
            
        