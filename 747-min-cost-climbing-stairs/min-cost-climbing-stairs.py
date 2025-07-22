class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp={}

        def fa(ind):
            if ind<2:
                return cost[ind]
            if ind in dp:
                return dp[ind]
            dp[ind]=cost[ind]+min(fa(ind-1),fa(ind-2))
            return dp[ind]
        cost.append(0)
        return fa(len(cost)-1)
            
        